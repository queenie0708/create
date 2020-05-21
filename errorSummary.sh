# ssh att@10.75.11.124 'cat /var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official@3/TestJob_BT1_MTBF_Api29_Official_Results/testResult_20200508_203243/all_errors2.csv' > ./all_errors2-101.csv
# ssh att@10.75.11.124 'cat /var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official/TestJob_BT1_MTBF_Api29_Official_Results/testResult_20200508_203140/all_errors2.csv' > ./all_errors2-154.csv
# ssh att@10.75.11.124 'cat /var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official@2/TestJob_BT1_MTBF_Api29_Official_Results/testResult_20200508_203117/all_errors2.csv' > ./all_errors2-308.csv
# ssh att@10.75.11.124 'cat /var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official@4/TestJob_BT1_MTBF_Api29_Official_Results/testResult_20200508_195526/all_errors2.csv' > ./all_errors2-437.csv
# ssh att@10.75.11.124 'cat /var/lib/jenkins-slave/workspace/Test_Jobs/TestJob_BT1_MTBF_Api29_Official@5/TestJob_BT1_MTBF_Api29_Official_Results/testResult_20200508_195600/all_errors2.csv' > ./all_errors2-477.csv
# cat *.csv > all.csv
# echo "merge file done"
cat all.csv | grep Tombstone | sort | uniq -c | sort -r > Tombstonecount.txt
echo "Counting tombstone..."
#sed 's/ Tombstone/,Tombstone/g' Tombstonecount.txt > Tombstonecount.txt  method too slow
#echo "Count tombstone done"
cat all.csv | grep App_crash | sort | uniq -c | sort -r > Crashcount.txt
echo "Counting crash..."
# sed 's/ App_crash/,App_crash/g'  > Crashcount.txt  method too slow
# echo "Count crash done"
cat all.csv | grep ANR | sort | uniq -c | sort -r > ANRcount.txt
echo "Counting ANR..."
# sed 's/ ANR/,ANR/g'  > ANRcount.txt  method too slow
echo "Count ANR done"
cat *count.txt > all_summary.csv
echo "merge summary done"