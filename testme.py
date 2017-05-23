from syncer.interactors import Blockchain, BlockchainSyncer
from syncer.gateways import MongoDatabaseGateway
from pymongo import MongoClient
from bitcoinrpc.authproxy import AuthServiceProxy
import ConfigParser
import redis

REDIS_CLIENT = redis.Redis()

config = ConfigParser.RawConfigParser()
config.read('/home/vagrant/.exploder/exploder.conf')

client = MongoClient()
database = MongoDatabaseGateway(client.exploder, config)
blockchain = Blockchain(database, config)

rpc_client = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"
                              % (config.get('syncer', 'rpc_user'), config.get('syncer', 'rpc_password')))
syncer = BlockchainSyncer(database, blockchain, rpc_client, config)
syncer.calculate_network_stats()
