from cassandra.query import SimpleStatement

from gsrest.db.cassandra import get_session
from gsrest.model.blocks import Block


BLOCKS_PAGE_SIZE = 100


def get_block(currency, height):
    session = get_session(currency, 'raw')

    query = "SELECT * FROM block WHERE height = %s"
    result = session.execute(query, [height])

    return Block(result[0]).__dict__ if result else None


def list_blocks(currency, paging_state=None):
    session = get_session(currency, 'raw')

    query = "SELECT * FROM block"
    statement = SimpleStatement(query, fetch_size=BLOCKS_PAGE_SIZE)
    results = session.execute(statement, paging_state=paging_state)

    paging_state = results.paging_state
    block_list = [Block(row).__dict__ for row in results.current_rows]

    return paging_state, block_list
