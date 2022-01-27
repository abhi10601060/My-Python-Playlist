def duplicate_subsequence(arr):
    ans = [[]]
    for i in range(len(arr)):

        if i != 0 and arr[i] == arr[i-1]:
            end1 = len(ans)
            for j in range(end, len(ans)):
                ans.append(ans[j]+[arr[i]])
            end = end1
            continue

        end = len(ans)

        for k in range(len(ans)):
            ans.append(ans[k]+[arr[i]])
    return ans


arr = [1, 2, 2,2]
print(duplicate_subsequence(arr))
