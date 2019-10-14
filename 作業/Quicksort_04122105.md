
作業 Quick Sort
===
日延A 04122105 高星瑜

什麼是 Quick Sort?
-----
在數列中任意挑選一個數作為基準點，然後調整數列，使得基準點左邊的數都比基準點小，右邊的數都比基準點大，此時基準點本身已經排列在正確位置。
再來，從原基準點左右兩個數列中，再各任意挑選一個數作為基準點，重複前述調整方法。反覆直到基準點左右無法分出新的數列為止，即完成排序。

Python 程式碼
-----


```python
def Quicksort:
    left = []
    equal = []
    right = []

    if len(array) > 1:
        pivot = array[0] #將基準點設定為數列中的第一個數
        for x in array:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                right.append(x)
        return sort(left)+equal+sort(right)  
    else:  
        return array
```

Quick Sort 時間複雜度
-----
Best Case：Ο(n log n) 
第一個基準值的位置剛好是中位數，將資料均分成二等份

Worst Case：Ο(n2)　 
當資料的順序恰好為由大到小或由小到大時，有分割跟沒分割一樣

Average Case：Ο(n log n)
