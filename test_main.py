import pytest
from main import add

@pytest.mark.asyncio
async def test_add():
    assert await add(2, 3) == {"total": 5}
    assert await add(0, 0) == {"total": 0}
    assert await add(-1, 1) == {"total": 0}