Heap sort/Merge sort比較
====
時間複雜度
----
|               |Heapsort       | Mergesort   |
| ------------- | ------------- |-------------|
|Best Case |Ο(n log n)|Ο(n log n)|
|Worst Case|Ο(n log n)|Ο(n log n)|
|Average Case|Ο(n log n)|Ο(n log n)|

Heapsort:
----
Heapify的部分，時間複雜度是Ο(log n)，然後再Heapsort時要倫過每一個節點(n)，所以Heapsort的總共時間複雜度是O(n log n)。  

Mergesort:
----
拆分時，n個數的數列要切n-1次。(n)  
而合併時，進行每一次的合併都要花O(n)，一次都是倆倆合併，所以每次合併的對數都會減半，共要合併O(log n)次。  
結合拆分與合併，Mergesort的總共時間複雜度是O(n log n)。  


空間複雜度
----
|Heapsort       | Mergesort   |
| ------------- |-------------|
 |Ο(1)|Ο(n)|
 
 Heapsort:
----
不需要額外的數列來儲存排列好的數，所以時間複雜度為O(1)。

Mergesort:
----
需要一個與原來數列一樣的額外空間，來暫時儲存每一回合的合併結果，故為O(n)。
  
  
    
     
     
     
參考資料  
[初學者學演算法-排序法進階-合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)  
[合併排序](https://kopu.chat/2017/08/10/%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F-merge-sort/)  
[HeapSort-GEEksforGeeks](https://www.geeksforgeeks.org/heap-sort/#:~:targetText=Heap%20sort%20is%20an%20in%2Dplace%20algorithm.&targetText=Time%20Complexity%3A%20Time%20complexity%20of,Sort%20is%20O(nLogn).)

