from datetime import datetime
import json
import predictors
import os.path
import traceback

class Updater(object):
    def __init__(self):
        with open('predictors.json','r') as f:
            self.predictors = json.load(f)

    def update_predicton(self,instance):
        file = 'predictions/' + instance.get_name() + '.json'
        rise = instance.goes_up()
        now = datetime.strftime(datetime.utcnow(), '%Y-%m-%d %H:%M:%S')

        # Creates data file for predictor if it does not yet exist
        if not os.path.isfile(file):
            predictions = [[now,rise]]

        # Otherwise, updates the data file for the respective predictor
        else:
            with open(file,'r') as f:
                predictions = json.load(f)
            predictions.append([now,rise])

        # Writes updated data back to file
        with open(file,'w') as f:
                json.dump(predictions,f)

    def update_all(self):
        # Goes through each predictor and updates it's respective data file
        # This needs to be continually kept up to date with predictors.json
        success = 0
        total = len(self.predictors)
        print "Updating all " + str(total) + " predictors."
        for predictor in self.predictors:
            predictorCall = getattr(predictors, predictor)
            instance = predictorCall()

            print "Updating " + predictor + " (" + str(self.predictors.index(predictor) + 1) + " of " + str(total) + ")"
            try:
                self.update_predicton(instance)
                success += 1
            except:
                print "Could not update " + predictor + "! Here is the traceback:"
                print traceback.format_exc()
        print "Updated " + str(success) + " of " + str(total) + " predictors."

if __name__ == "__main__":
    Updater().update_all()
