import pickle
from feedly.serializers.base import BaseSerializer, BaseAggregatedSerializer


class PickleSerializer(BaseSerializer):

    def loads(self, serialized_activity):
        activity = pickle.loads(serialized_activity)
        return activity

    def dumps(self, activity):
        self.check_type(activity)
        return pickle.dumps(activity)


class AggregatedActivityPickleSerializer(BaseAggregatedSerializer):
    #: indicates if dumps returns dehydrated aggregated activities
    dehydrate = True
    
    def loads(self, serialized_data):
        return pickle.loads(serialized_data)

    def dumps(self, aggregated):
        self.check_type(aggregated)
        dehydrated_aggregated = aggregated.get_dehydrated()
        return pickle.dumps(dehydrated_aggregated)