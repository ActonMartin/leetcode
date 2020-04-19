#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = list(a)
        list_b = list(b)
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            short_list = len_a
            long_list = len_b
            flag = 0
            for i in range(short_list-1, -1, -1):
                gap_b = i +long_list -short_list
                if int(a[i]) + int(b[gap_b])  < 2 and flag ==0:
                    list_b[gap_b] = int(a[i]) + int(b[gap_b]) + flag
                    flag = 0
                elif int(a[i]) + int(b[gap_b]) == 2 and flag ==0:
                    list_b[gap_b] = 0
                    flag = 1
                elif int(a[i]) + int(b[gap_b]) < 2 and flag ==1:
                    if int(a[i]) + int(b[gap_b]) + flag < 2:
                        list_b[gap_b] = int(a[i]) + int(b[gap_b]) + flag
                        flag = 0
                    else:
                        list_b[gap_b] = 0
                        flag = 1
                elif int(a[i]) + int(b[gap_b]) == 2 and flag ==1:
                    list_b[gap_b] = 1
                    flag = 1

            for j in range(long_list-short_list-1, -1, -1):

                if int(list_b[j]) + flag  < 2:
                    list_b[j] = int(list_b[j]) + flag 
                    flag = 0
                else:
                    list_b[j] = 0 
                    flag = 1
            if flag == 1:
                xxx = "1"
                for val in list_b:
                    xxx +=str(val)
                return xxx
            else:
                xxx = ""
                for val in list_b:
                    xxx +=str(val)
 
                return xxx
        elif len_a > len_b:
            short_list = len_b
            long_list = len_a
            flag = 0
            for i in range(short_list-1, -1, -1):
                gap_a = i +long_list -short_list
                if int(a[gap_a]) + int(b[i])  < 2 and flag ==0:
                    list_a[gap_a] = int(a[gap_a]) + int(b[i]) + flag
                    flag = 0
                elif int(a[gap_a]) + int(b[i]) == 2 and flag ==0:
                    list_a[gap_a] = 0
                    flag = 1
                elif int(a[gap_a]) + int(b[i]) < 2 and flag ==1:
                    if int(a[gap_a]) + int(b[i]) + flag < 2:
                        list_a[gap_a] = int(a[gap_a]) + int(b[i]) + flag
                        flag = 0
                    else:
                        list_a[gap_a] = 0
                        flag = 1
                elif int(a[gap_a]) + int(b[i]) == 2 and flag ==1:
                    list_a[gap_a] = 1
                    flag = 1

            for j in range(long_list-short_list-1, -1, -1):
                if int(list_a[j]) + flag  < 2:
                    list_a[j] = int(list_a[j]) + flag 
                    flag = 0
                else:
                    list_a[j] = 0 
                    flag = 1

            if flag ==1:
                xxx ="1"
                for val in list_a:
                    xxx +=str(val)

                return xxx
            else:
                xxx =""
                for val in list_a:
                    xxx += str(val)

                return xxx
        
        else:
            flag = 0
            for i in range(len_a-1, -1, -1):

                if int(a[i]) + int(b[i])  < 2 and flag ==0:
                    list_a[i] = int(a[i]) + int(b[i]) + flag
                    flag = 0
 
                elif int(a[i]) + int(b[i]) == 2 and flag ==0:
                    list_a[i] = 0
                    flag = 1

                elif int(a[i]) + int(b[i]) < 2 and flag ==1:
                    if int(a[i]) + int(b[i]) + flag < 2:
                        list_a[i] = int(a[i]) + int(b[i]) + flag
                        flag = 0
                    else:
                        list_a[i] = 0
                        flag = 1
                elif int(a[i]) + int(b[i]) == 2 and flag ==1:
                    list_a[i] = 1
                    flag = 1

            if flag == 1:
                xxx = "1"
                for val in list_a:
                    xxx += str(val)

                return xxx
            else:
                xxx = ""
                for val in list_a:
                    xxx += str(val)
                return xxx
        
       
# @lc code=end

