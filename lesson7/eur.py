moving_average=[1.12512,1.12388,1.12441,1.12409,1.13085,1.12730,1.13298,1.12847,1.13001,1.12999,1.13428,1.13996,1.14114,1.13836,1.14396,1.14115,1.14472,1.15266,1.15695,1.15960,1.16410,1.16393,1.17510,1.17155,1.17913,1.18470,1.17785,1.17684,1.17620,1.18020,1.18629,1.18768,1.17883,1.17857,1.17374,1.17399,1.17840,1.18128,1.18356,1.18378,1.18702,1.19307,1.18374,1.18600,1.17940,1.17889,1.17875,1.18341,1.18299,1.18216,1.18980,1.18966,1.19360,1.19116,1.18545,1.18512,1.18426,1.18458,1.18143,1.17733,1.18027,1.18144,1.18413,1.18319,1.18666,1.18460,1.18157,1.18478,1.18494,1.18350,1.17704,1.17077,1.16597,1.16721,1.16260,1.16194,1.16652,1.17430,1.17200,1.17451,1.17108,1.17105,1.17831,1.17338,1.17622,1.17650]
total=sum(moving_average)
size=(len(moving_average))
print(total/size)
print(1.20104-1.11870)
 
import statistics
median = statistics.median(moving_average)
print(median)
 
print("mode of given data set is % s" %(statistics.mode(moving_average)))
 