#Python3

with open("covid.txt", "a+") as myfile:
    myfile.write("\nNorthern Railway has made available 503 isolation coaches equivalent to 8,048 beds as COVID Care Centres at nine stations in Delhi. These stations include Anand Vihar Terminal, Shakurbasti, Sarai Rohilla, Safdarjung, Shahdara, Adarsh Nagar, Delhi Cantt, Badli and Tughlakabad.")
    myfile.write("\nUnder the guidance of the Centre, the State and UT governments have ramped up the testing and hospital infrastructure by combining public and private sector efforts. Many States have conducted the population surveys to map and identify the vulnerable population like the elderly, pregnant women and those with co-morbidities. Health Ministry said, at the ground level, front line health workers like ASHAs and ANMs have done a commendable job of managing the migrant population and to enhance awareness at the community level. As a result, there are 29 States and UTs with Case Fatality Rate lower than the India average. Five States and UTs have a Zero Case Fatality Rate. While 14 States and UTs have a Case Fatality Rate of less than one per cent.")
    content = myfile.read()

print(content)
