import yaml
import os.path
from subscripts import aboutyou, yourdrivers, yourvehicles

configData = {'Iterations': 0}
iterations = None
output = None
testID = None

if os.path.isfile("config.yaml"):
    with open('config.yaml') as f:
        configData = yaml.safe_load(f)
else:
    with open('config.yaml', 'w') as f:
        yaml.dump(configData, f, default_flow_style=False)
    quit()

for i in range(configData['Iterations']):
    output = aboutyou.makeList()
    testID = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
    list.insert(output, 0, testID)
    print(output)

#Test Case field - This has to be a mix of Test case identifier + Scenario Type + Type of Application + Vehicle Driver Combinations + State
#Example : TC001-E2E-Web-1V1D-AL - This has Test Case Name+Numric Number (3 digits) and followed by the above mentioned combination.
#So for the next test case, the sequence changes to 002 and Test case name is TC002-E2E-Web-1V1D-MS