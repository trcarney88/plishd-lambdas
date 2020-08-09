import arrow
import SendReminderEmail

''' Tests the Get Wait Time function of SendReminderEmail '''
input = {}
output = []

''' Inputs for testing '''
# Daily Tests
input[0] = {'time': "16:00:00", 'date': "2020-01-31T16:00:50.683122-07:00", 'interval': "D"}
input[1] = {'time': "16:00:00", 'date': "2019-02-28T16:00:50.683122-07:00", 'interval': "D"}
input[2] = {'time': "16:00:00", 'date': "2020-02-29T16:00:50.683122-07:00", 'interval': "D"}
input[3] = {'time': "16:00:00", 'date': "2020-03-31T16:00:50.683122-07:00", 'interval': "D"}
input[4] = {'time': "16:00:00", 'date': "2020-04-30T16:00:50.683122-07:00", 'interval': "D"}
input[5] = {'time': "16:00:00", 'date': "2020-05-31T16:00:50.683122-07:00", 'interval': "D"}
input[6] = {'time': "16:00:00", 'date': "2020-06-30T16:00:50.683122-07:00", 'interval': "D"}
input[7] = {'time': "16:00:00", 'date': "2020-07-31T16:00:50.683122-07:00", 'interval': "D"}
input[8] = {'time': "16:00:00", 'date': "2020-08-31T16:00:50.683122-07:00", 'interval': "D"}
input[9] = {'time': "16:00:00", 'date': "2020-09-30T16:00:50.683122-07:00", 'interval': "D"}
input[10] = {'time': "16:00:00", 'date': "2020-10-31T16:00:50.683122-07:00", 'interval': "D"}
input[11] = {'time': "16:00:00", 'date': "2020-11-30T16:00:50.683122-07:00", 'interval': "D"}
input[12] = {'time': "16:00:00", 'date': "2020-12-31T16:00:50.683122-07:00", 'interval': "D"}

# Monthly Tests
input[13] = {'time': "16:00:00", 'date': "2020-01-01T16:00:50.683122-07:00", 'interval': "M"}
input[14] = {'time': "16:00:00", 'date': "2020-02-01T16:00:50.683122-07:00", 'interval': "M"}
input[15] = {'time': "16:00:00", 'date': "2020-03-01T16:00:50.683122-07:00", 'interval': "M"}
input[16] = {'time': "16:00:00", 'date': "2020-04-01T16:00:50.683122-07:00", 'interval': "M"}
input[17] = {'time': "16:00:00", 'date': "2020-05-01T16:00:50.683122-07:00", 'interval': "M"}
input[18] = {'time': "16:00:00", 'date': "2020-06-01T16:00:50.683122-07:00", 'interval': "M"}
input[19] = {'time': "16:00:00", 'date': "2020-07-01T16:00:50.683122-07:00", 'interval': "M"}
input[20] = {'time': "16:00:00", 'date': "2020-08-01T16:00:50.683122-07:00", 'interval': "M"}
input[21] = {'time': "16:00:00", 'date': "2020-09-01T16:00:50.683122-07:00", 'interval': "M"}
input[22] = {'time': "16:00:00", 'date': "2020-10-01T16:00:50.683122-07:00", 'interval': "M"}
input[23] = {'time': "16:00:00", 'date': "2020-11-01T16:00:50.683122-07:00", 'interval': "M"}
input[24] = {'time': "16:00:00", 'date': "2020-12-01T16:00:50.683122-07:00", 'interval': "M"}

# Quarterly Tests
input[25] = {'time': "16:00:00", 'date': "2020-01-01T16:00:50.683122-07:00", 'interval': "Q"}
input[26] = {'time': "16:00:00", 'date': "2020-04-01T16:00:50.683122-07:00", 'interval': "Q"}
input[27] = {'time': "16:00:00", 'date': "2020-07-01T16:00:50.683122-07:00", 'interval': "Q"}
input[28] = {'time': "16:00:00", 'date': "2020-10-01T16:00:50.683122-07:00", 'interval': "Q"}

# Semi Annual Tests
input[29] = {'time': "16:00:00", 'date': "2020-01-01T16:00:50.683122-07:00", 'interval': "SA"}
input[30] = {'time': "16:00:00", 'date': "2020-07-01T16:00:50.683122-07:00", 'interval': "SA"}

# Annual Test
input[31] = {'time': "16:00:00", 'date': "2020-01-01T16:00:50.683122-07:00", 'interval': "A"}

# Weekly Test
input[32] = {'time': "16:00:00", 'date': "2019-12-27T16:00:50.683122-07:00", 'interval': "W"}

''' Expected results from the inputs above '''
# Daily Test Results
output.append("2020-02-01T16:00:00-07:00")
output.append("2019-03-01T16:00:00-07:00")
output.append("2020-03-01T16:00:00-07:00")
output.append("2020-04-01T16:00:00-07:00")
output.append("2020-05-01T16:00:00-07:00")
output.append("2020-06-01T16:00:00-07:00")
output.append("2020-07-01T16:00:00-07:00")
output.append("2020-08-01T16:00:00-07:00")
output.append("2020-09-01T16:00:00-07:00")
output.append("2020-10-01T16:00:00-07:00")
output.append("2020-11-01T16:00:00-07:00")
output.append("2020-12-01T16:00:00-07:00")
output.append("2021-01-01T16:00:00-07:00")

# Monthly Test Results
output.append("2020-02-01T16:00:00-07:00")
output.append("2020-03-01T16:00:00-07:00")
output.append("2020-04-01T16:00:00-07:00")
output.append("2020-05-01T16:00:00-07:00")
output.append("2020-06-01T16:00:00-07:00")
output.append("2020-07-01T16:00:00-07:00")
output.append("2020-08-01T16:00:00-07:00")
output.append("2020-09-01T16:00:00-07:00")
output.append("2020-10-01T16:00:00-07:00")
output.append("2020-11-01T16:00:00-07:00")
output.append("2020-12-01T16:00:00-07:00")
output.append("2021-01-01T16:00:00-07:00")

# Quarterly Test
output.append("2020-04-01T16:00:00-07:00")
output.append("2020-07-01T16:00:00-07:00")
output.append("2020-10-01T16:00:00-07:00")
output.append("2021-01-01T16:00:00-07:00")

# Semi Annual Test
output.append("2020-07-01T16:00:00-07:00")
output.append("2021-01-01T16:00:00-07:00")

# Annual Test
output.append("2021-01-01T16:00:00-07:00")

# Weekly Test
output.append("2020-01-03T16:00:00-07:00")

result = True
for i in range(len(input)):
    out = SendReminderEmail.getWaitTime(input[i]['time'], input[i]['date'], input[i]['interval']) 
    if out != output[i]:
        print("Failed Test. Expected: " + output[i] + " Got: " + out)
        result = False

print("Ran " + str(i+1) + " tests.")

if result:    
    print("All tests passed!")