# Copyright 2012 10gen, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Motor benchmarking suite, using tornado.gen.engine."""

import sys

from tornado import gen
import motor

sys.path[0:0] = [""]

# Import these names so they're available to main()
from async_common import run
from benchmark_common import per_trial, batch_size, main


@gen.engine
def insert(callback, db, collection, object):
    """Unsafe inserts"""
    for i in range(per_trial):
        to_insert = object.copy()
        to_insert["x"] = i
        yield motor.Op(db[collection].insert, to_insert)
    callback()

""" see https://github.com/mongodb/motor/blob/master/doc/changelog.rst """
# @gen.coroutine
# def insert_batch(callback, db, collection, object):
#     f= db[collection].insert([object] * batch_size)
#     for i in range(per_trial / batch_size):
#         yield [f]
#     callback()
#     return
# @gen.engine
# def insert_batch(callback, db, collection, object):
#     for i in range(per_trial / batch_size):
#         yield motor.Op(db[collection].insert, [object] * batch_size)
#     callback()
def insert_batch(callback, db, collection, object):
    callback()

@gen.engine
def find_one(callback, db, collection, x):
    for _ in range(per_trial):
        yield motor.Op(db[collection].find_one, {"x": x})
    callback()


# @gen.engine
# def find(callback, db, collection, x):
#     for _ in range(per_trial):
#         yield motor.Op(db[collection].find({"x": x}).to_list)
#     callback()

def find(callback, db, collection, x):
    callback()


if __name__ == "__main__":
    #trial_db = motor.MotorClient().open_sync().benchmark
    trial_db = motor.MotorClient(host='127.0.0.1', max_pool_size=6000, connectTimeoutMS=None).benchmark
    main(globals())
