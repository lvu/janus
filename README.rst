=======
 janus
=======
.. image:: https://travis-ci.org/aio-libs/janus.svg?branch=master
    :target: https://travis-ci.org/aio-libs/janus
.. image:: https://codecov.io/gh/aio-libs/janus/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/aio-libs/janus
.. image:: https://img.shields.io/pypi/v/janus.svg
    :target: https://pypi.python.org/pypi/janus
.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/aio-libs/Lobby
    :alt: Chat on Gitter



Mixed sync-async queue, supposed to be used for communicating between
classic synchronous (threaded) code and asynchronous (in terms of
asyncio_) one.

Like `Janus god <https://en.wikipedia.org/wiki/Janus>`_ the queue
object from the library has two faces: synchronous and asynchronous
interface.

Synchronous is fully compatible with `standard queue
<https://docs.python.org/3/library/queue.html>`_, asynchronous one
follows `asyncio queue design
<https://docs.python.org/3/library/asyncio-queue.html>`_.

Usage example
=============

.. code:: python

    import asyncio
    import janus

    loop = asyncio.get_event_loop()
    queue = janus.Queue(loop=loop)


    def threaded(sync_q):
        for i in range(100):
            sync_q.put(i)
        sync_q.join()


    async def async_coro(async_q):
        for i in range(100):
            val = await async_q.get()
            assert val == i
            async_q.task_done()


    fut = loop.run_in_executor(None, threaded, queue.sync_q)
    loop.run_until_complete(async_coro(queue.async_q))
    loop.run_until_complete(fut)


Communication channels
======================

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Feel free to post your questions and ideas here.

*gitter chat* https://gitter.im/aio-libs/Lobby


License
=======

``janus`` library is offered under Apache 2 license.

Thanks
======

The library development is sponsored by DataRobot (https://datarobot.com)

.. _asyncio: https://docs.python.org/3/library/asyncio.html
