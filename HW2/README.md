HW 2
====
Heap Sort & Merge Sort
----

Heap Sort  
一個堆(Heap)的結構:  
1.會是一個二元樹(Binary tree)，每一個子樹中的父節點的值必須大於它的兩個子節點。  
2.節點生成方式一定為由上往下，由左往右。  
3.當前節點位置為i時，它的父節點位置就會是(i-1)/2整除部分的位置。  
4.當前節點位置為i時，它的兩個子節點(c1與c2)位置分別會是2i+1, 2i+2。  
  
Heapify的概念:  
將一個節點作為父節點出發，若父節點沒有比它的子節點大，則將較大的子節點跟父節點做交換，  
接著再對交換過的子節點再做Heapify，直到當前的節點(位置為i)已經沒有子節點(2i+1已經大於數列長度n)。  
   
Build Heap建構一個結構正確的堆:  
因為前述的Heapify的特點，若要數列中所有數字都符合Heap的結構，需要再經過整理。  
從最後一個節點的父節點開始往前依次做Heapify，才能確保所有節點都經過整理。    
在建完一個堆之後，才能作Heap Sort。  
  
Heapsort 堆排序概念:  
將最前面的根節點與樹中最後一個節點作交換，再將最後一個節點排到新的數列中。   
此時最小的數會在根節點位置，不符合Heap結構，所以再從這個節點作一次Heapify，最大值將會再次在節點的位置。  
依此循環，直到所有數都排序好，即完成Heapsort。  
  
Merge Sort  
Merge 合併概念:  
將兩個已排序好的數列A、B合併成新的數列C。  
合併方法:  
從AB兩數列分別的第一位數字開始比較，  
若A[0]<B[0]，則將A[0]放進C。接著比較A數列的第二個數跟B數列的第一個數;  
若B[0]<A[0]，則將B[0]放進C。接著比較A數列的第一個數跟B數列的第二個數。  
->以此往下做比較，將當前比較的數，值較小的放在C數列。  
有較小值的數列，其比較位數往後移一位，再與另一數列的數字做比較。  
直到有一邊的數列沒有下一個數了，剩下的數字可以直接放入C數列中(因為兩數列自身已經排序過)，完成合併。  
  
拆分概念:  
將一個完整的數列，從中間拆成左右兩個數列，再將拆好的數列分別再次分為左右兩個數列，  
以此循環直到每個數列都只剩下一個數。  
  
Merge Sort: 先拆分，再合併  
先將要排序的數列，拆分成多個長度為一的數列，再將數列兩兩合併，  
合併完的數列再兩兩合併，直到全部合併為一個數列，即完成Merge Sort。  
