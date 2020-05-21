# import pandas as pd # 引用套件並縮寫為 pd  
# df = pd.read_csv('all_summary.csv',error_bad_lines=False)  
# print(df)  
text = open("all_errors2-477.csv", "r")
text = ''.join([i for i in text]) \
    .replace("/var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official@5/TestJob_BT1_MTBF_Api29_Official_Results/", r"\\10.75.10.254\mtbf\BT1\V0.150\1040339020000477\TestJob_BT1_MTBF_Api29_Official_59") \
    .replace(r'/','\\') 
x = open("all_new.csv","w")
x.writelines(text)
x.close()