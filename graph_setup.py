from langchain_neo4j import Neo4jGraph
from config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

def setup_graph():
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )

    movies_query = """
   
    LOAD CSV WITH HEADERS FROM
    './dataset/movie.csv' AS row
    MERGE (m:Movie {id:row.MovieID})
    SET m.released = date(row.Release_Date),
        m.title = row.Title,
        m.imdbRating = toFloat(row.Vote_Average)
    FOREACH (director in split(row.Director, ', ') |
        MERGE (p:Person {name:trim(director)})
        MERGE (p)-[:DIRECTED]->(m))
    FOREACH (actor in split(row.Cast, ', ') |
        MERGE (p:Person {name:trim(actor)})
        MERGE (p)-[:ACTED_IN]->(m))
    FOREACH (genre in split(row.Genres, ', ') |
        MERGE (g:Genre {name:trim(genre)})
        MERGE (m)-[:IN_GENRE]->(g))
    """
    graph.query(movies_query)
    graph.refresh_schema()
    return graph
