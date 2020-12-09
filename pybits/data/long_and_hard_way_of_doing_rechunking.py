from __future__ import division
from itertools import chain
from numpy import inf
from span.chunking.utils.fixed_step import fixed_step_chunker
import random


def fragment_list(tot_len, n_frags):
    """
    A little function to help trouble shoot list_chunker. Creates a list of lists
    by randomly fragmenting range(tot_len) into n_frags list

    Args:
        tot_len: the total number of elements in the lists
        n_frags: the number of lists

    Returns: a list of list
    """

    indices = random.sample(range(tot_len), n_frags)
    indices.sort()
    start = 0
    list_of_list = []
    for i in range(n_frags):
        list_of_list.append(range(start, indices[i], 1))
        start = indices[i]
    list_of_list.append(range(indices[n_frags - 1], tot_len, 1))

    return [item for item in list_of_list if len(item) > 0]


def list_frag(list_to_frag):

    """

    Args:
        list_to_frag: any list

    Returns: a random partition of list_to_frag in a form of a list of sublists covering list_to_frag

    """

    lile = len(list_to_frag)
    n_frags = random.randint(1, lile)
    indices = random.sample(range(lile), n_frags)
    indices.sort()
    start = 0
    frag_list = []
    for i in range(n_frags):
        frag_list.append(list_to_frag[start:indices[i]])
        start = indices[i]
    frag_list.append(list_to_frag[indices[n_frags - 1]:])

    return [item for item in frag_list if len(item) > 0]


def rand_sub(list_of_list, list_objects):

    random.seed(8128)
    for l in range(len(list_of_list)):
        for item in range(len(list_of_list[l])):
            list_of_list[l][item] = random.choice(list_objects)
    return list_of_list


def list_chunker(list_it, chk_size, chk_step=None, start_at=0, stop_at=None, return_tail=False):
    """
      a function to get (an iterator of) segments (bt, tt) of chunks from the iterator of lists, of the form
      list_it = [[list_1], [list_2], ...] where the list_1, list_2...may have different lengths
      :param list_it: iterator of lists, for example [[1,2], [3,4,5], [6], ...]
      :param chk_size: length of the chunks
      :param chk_step: step between chunks
      :param start_at: value from the iterator at which we begin building the chunks (inclusive)
      :param stop_at: last value from the iterator included in the chunks (exclusive)
      :param return_tail: if set to false, only the chunks with max element less than stop_at are yielded
      if set to true, any chunks with min value no more than stop_at are returned but they contain values no more
      than stop_at
      :return: an iterator of the chunks

      1) If stop_at is not None and return_tail is False:
         will return all full chunks with maximum element index less than stop_at
         or until the iterator is exhausted. Only full chunks are returned here.

      2) If stop_at is not None and return_tail is True:
         will return all full chunks as above along with possibly cut off chunks
         containing one term whose index is stop_at-1 or one (last) term which is the
         last element of it

      3) If stop_at is None and return_tail is False:
         will return all full chunks with maximum element index less or equal to the last
         element of it

      4) If stop_at is None and return_tail is True:
         will return all full chunks with maximum element index less or equal to the last
         element of it plus cut off chunks whose maximum term index is the last term of it

    # the next two examples show the difference between return_tail = True or False
    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=1, start_at=0, stop_at=None, return_tail=True)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14], [14]]

    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=1, start_at=0, stop_at=None, return_tail=False)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14]]

    # start_at is set to 2: we remove the first two terms (index 0 and index 1)
    # stop_at is set to 5: we remove any terms of index 5 or more
    # return_tail is true: we yield the partial chunks as well
    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=1, start_at=2, stop_at=5, return_tail=True)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[2, 3, 4], [3, 4], [4]]

    # same as above with return_tail=False: no partial chunk yielded
    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=1, start_at=2, stop_at=5, return_tail=False)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[2, 3, 4]]

    # chk_step > chk_size in the next 4 examples
    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=6, start_at=5, stop_at=15, return_tail=False)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[5, 6, 7], [11, 12, 13]]

    >>> list_it = fragment_list(15, 5)
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=4, start_at=2, stop_at=15, return_tail=True)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[2, 3, 4], [6, 7, 8], [10, 11, 12], [14]]

    >>> list_it = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11], [12, 13, 14, 15, 16], [17], [18], [19]]
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=6, start_at=5, stop_at=None, return_tail=True)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[5, 6, 7], [11, 12, 13], [17, 18, 19]]

    >>> list_it = [[0, 1], [2], [3, 4, 5], [6, 7, 8], [9, 10], [11], [12, 13, 14], [15, 16, 17, 18, 19]]
    >>> f = lambda it: list_chunker(it, chk_size=3, chk_step=6, start_at=5, stop_at=None, return_tail=True)
    >>> A = list(f(list_it)); B = list(f(iter(list_it)));  # trying the function on it (a list) and iter(it) (and iterator)
    >>> assert A == B  # list_it and iter(list_it) should give the same thing!
    >>> A  # and that thing is:
    [[5, 6, 7], [11, 12, 13], [17, 18, 19]]


    """

    if chk_step is None:
        chk_step = chk_size

    if stop_at is not None:
        assert isinstance(stop_at, int), 'stop_at should be an integer'

    # setting the start_at to the first element of the iterator by default
    if start_at is None:
        start_at = 0

    if hasattr(list_it, '__getslice__'):

        # flatten the list and use fast_chunker
        list_it = list(chain.from_iterable(list_it))
        for x in fixed_step_chunker(list_it, chk_size, chk_step, start_at, stop_at, return_tail):
            yield x

    else:

        # we set stop_at to be infinity by default
        if stop_at is None:
            stop_at = inf

        # in that case, nothing to return
        if stop_at - start_at < chk_size and not return_tail:
            return

        # getting the first list
        buff = list_it.next()

        # consuming list_it until we reach start_at
        if start_at is not None:
            position = 0
            while position < start_at:
                if position + len(buff) < start_at:
                    position += len(buff)
                    buff = list_it.next()
                else:
                    buff = buff[start_at - position:]
                    position = start_at
                    break

        # checking a few things
        assert isinstance(chk_size, int) and chk_size > 0, 'chk_size should be a positive interger'
        assert isinstance(chk_step, int) and chk_step > 0, 'chk_step should be a positive integer'
        assert isinstance(start_at, int), 'start_at should be an integer'
        assert stop_at > start_at, 'stop_at should be larger than start_at'

        # in that case only tails are returned
        if stop_at - start_at < chk_size and return_tail:
            while len(buff) < stop_at - start_at:
                try:
                    buff = buff + list_it.next()
                except StopIteration:
                    break

            # could use fast_chunker to finish the job with:
            # for x in fast_chunker(buffer, chk_size, chk_step, start_at, stop_at, return_tail):
            #     yield x
            if stop_at != inf:
                buff = buff[:stop_at - start_at]

            while len(buff) > 0:
                yield buff
                buff = buff[chk_step:]

        elif chk_step <= chk_size:
            # stop will keep track of whether the iterator is consumed
            stop = False
            # par_stop_at will become the parameter of chunker, since fast_chunker does not accept inf
            # as a parameter. Could possible modify chunker instead
            if stop_at == inf:
                par_stop_at = None
            else:
                par_stop_at = stop_at - start_at

            # if the buffer already exceeds stop_at, we just use chunker right away to conclude
            if len(buff) > stop_at - start_at:
                for x in fixed_step_chunker(buff, chk_size=chk_size, chk_step=chk_step, start_at=None,
                                 stop_at=par_stop_at, return_tail=return_tail):
                    yield x
                return

            # otherwise, we can start yielding chunks
            else:
                while not stop:
                    # consume the present buffer
                    while len(buff) > chk_size:
                        yield buff[:chk_size]
                        buff = buff[chk_step:]
                        position += chk_step
                    # attempt to extend the buffer when running out
                    try:
                        buff = buff + list_it.next()
                        # if the max of the buffer is larger than stop_at, we escape the current loop
                        # we shorten the buffer to make sure we do not return chunks past stop_at
                        if position + len(buff) > stop_at - 1:
                            buff = buff[:stop_at - position]
                            stop = True
                    # if we run out of list in list_it, we escape the current loop
                    except StopIteration:
                        stop = True

                    # we are in a position where the current buffer will be our last
                    # since we either ran out of list or reach the stop_at
                    # and thus we just finish to consume the current buffer
                    while len(buff) >= chk_size:
                        yield buff[:chk_size]
                        buff = buff[chk_step:]
                        position += chk_step

            # returning the tails
            if return_tail:
                while len(buff) > 0 and position < stop_at:
                    if stop_at != inf:
                        yield buff[:stop_at - position]
                    else:
                        yield buff
                    buff = buff[chk_step:]

        # case when chk_step > chk_size
        else:
            # stop will keep track of whether the iterator is consumed or whether the stop_at has been reached
            stop = False
            # par_stop_at will become the parameter of chunker, since fast_chunker does not accept inf
            # as a parameter. Could possible modify chunker instead
            if stop_at == inf:
                par_stop_at = None
            else:
                par_stop_at = stop_at - position

            # if the buffer already exceeds stop_at, we just use chunker right away to conclude
            if len(buff) > stop_at - start_at:
                for x in fixed_step_chunker(buff, chk_size=chk_size, chk_step=chk_step, start_at=0,
                                 stop_at=par_stop_at, return_tail=return_tail):
                    yield x
                return

            # otherwise, we can start yielding chunks
            else:
                while not stop:
                    # consume the present buffer
                    while len(buff) > chk_step:
                        yield buff[:chk_size]
                        buff = buff[chk_step:]
                        position += chk_step
                    # attempt to extend the buffer when running out in buff
                    try:
                        buff = buff + list_it.next()
                        # if the max of the buffer is larger than stop_at, we escape the current loop
                        # we shorten the buffer to make sure we do not return chunks past stop_at
                        if position + len(buff) - 1 >= stop_at:
                            buff = buff[:stop_at - position]
                            stop = True
                    # if we run out of list in list_it, we escape the current loop
                    except StopIteration:
                        stop = True

                    # we are in a position where the current buffer will be our last
                    # since we either ran out of list or reach the stop_at
                    # and thus we just finish to consume the current buffer
                    while len(buff) >= chk_step:
                        yield buff[:chk_size]
                        buff = buff[chk_step:]
                        position += chk_step

            if not return_tail and len(buff) >= chk_size and position + chk_size - 1 < stop_at:
                yield buff[:chk_size]

            # returning the tails
            if return_tail:
                while len(buff) > 0 and position < stop_at:
                    yield buff[: min(chk_size, stop_at - position)]
                    if len(buff) > chk_step:
                        buff = buff[chk_step:]
                        position += chk_step
                    else:
                        break

