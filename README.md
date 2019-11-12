# 資料結構與演算法 學習筆記
04122105 高星瑜

# HW 2
1. [Heap Sort程式碼](https://github.com/starfish8681/starfish8681/blob/master/HW2/heap_sort_04122105.py)  
2. [Merge Sort程式碼](https://github.com/starfish8681/starfish8681/blob/master/HW2/merge_sort_04122105.py)    
3. [Heap Sort文字說明](https://github.com/starfish8681/starfish8681/blob/master/HW2/Heapsort%E6%8F%8F%E8%BF%B0.ipynb)  
[Build Heap流程圖](https://github.com/starfish8681/starfish8681/blob/master/Week%208/BuildHeap.jpg)
. [Heap Sort流程圖](https://github.com/starfish8681/starfish8681/blob/master/Week%208/Heapsort.jpg)  
[nbviewer](https://nbviewer.jupyter.org/github/starfish8681/starfish8681/blob/master/HW2/Heapsort%E6%8F%8F%E8%BF%B0.ipynb)
4. [Merge Sort文字說明](https://github.com/starfish8681/starfish8681/blob/master/HW2/mergesort%E6%8F%8F%E8%BF%B0.ipynb)  
[Merge流程圖](https://github.com/starfish8681/starfish8681/blob/master/Week%208/Merge.jpg)
. [Divide流程圖](https://github.com/starfish8681/starfish8681/blob/master/Week%208/Divide.jpg)  
[nbviewer](https://nbviewer.jupyter.org/github/starfish8681/starfish8681/blob/master/HW2/mergesort%E6%8F%8F%E8%BF%B0.ipynb)
5. [Heap Sort/Merge Sort比較](https://github.com/starfish8681/starfish8681/blob/master/HW2/Heap%20sort,%20Merge%20sort%E6%AF%94%E8%BC%83.md)

---
- [Week 2](#week-2) :  
[Linked List.py](https://github.com/starfish8681/starfish8681/blob/master/Week%202/Linked_list.py)  
- [Week 3](#Week-3) :  
[Queue.py](https://github.com/starfish8681/starfish8681/blob/master/Week%203/implement-queue-using-stacks.py)
. [Stack,py](https://github.com/starfish8681/starfish8681/blob/master/Week%203/mini%20stack.py)
- [Week 4](#week-4) :  
[Insertion Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%204/Insertion%20Sort.py)
. [HW1-Quick Sort](https://github.com/starfish8681/starfish8681/blob/master/HW1/Quicksort_04122105.ipynb)
- [Week 6](#week-6) :  
[Quick Sort_Recursive.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Quick%20Sort_Recursive.py)
. [Heap Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Heap%20Sort.py)
. [Merge Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Merge%20Sort.py)
- [Week 8](#week-8) :  
[Binary Tree_Linked Structure.py](https://github.com/starfish8681/starfish8681/blob/master/Week%208/Binary%20Tree_Linked%20Structure.py)  
- [Week 9](#week-9) :  
[Binary Search Tree]()
- [Week 10](#week-10) :  
[Red Black Tree.py](https://github.com/starfish8681/starfish8681/blob/master/Week%2010/Red%20Black%20Tree.py)
---
# Week 2  
Linked_list
----
- Linked-list介紹:  
Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向None。  
因此，每個節點本身應該要有兩種屬性（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標（pointer）。  
- 與Array的差別:  
陣列使用一連串的記憶體位置，因此可以透過array[index]直接存取資料，  
但是相對的，若要在陣列中加入或是刪除元素，則需要大量的資料搬移。  
而Linked-list的資料則散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成，  
但是相對的，在資料的讀取上比較適合循序的使用，無法直接取得特定順序的值（比如說沒辦法直接知道list[3]）。  
  
- 參考資料: [用python實作linked-list](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)

---
# Week 3  
Queue
----
佇列，先進先出。
- Push  
在佇列中加入元素。  
- Pop  
將最前面(最先放入)的元素取出。  
- Peek  
回應最前面的元素。  
- Empty   
回應數列是否為空。  

Stack
----
堆疊，先進後出。
- Push  
新增一個新的元素到頂。
- Pop  
將最後面(最後放入)的元素取出。  
- Top  
回應頂端元素。

---
# Week 4  
Insertion Sort  
----
- Insertion Sort介紹:  
插入排序法（Insertion sort）為將數列分成排序與未排序兩部分，  
未排序數列中的數與已排序數列中之數比較大小，  
並把其插入已排序數列中適當的位置，比該數大的值則向右（後）移動。  
  
- 參考資料: [插入排序法](http://jialin128.pixnet.net/blog/post/141019829-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88insertion-sort%EF%BC%89in-pytho)
---
# Week 6  
Quick Sort  
----
- Quick Sort介紹:  
在數列中任意挑選一個數作為基準點，然後調整數列，使得基準點左邊的數都比基準點小，右邊的數都比基準點大，此時基準點本身已經排列在正確位置。  
再來，從原基準點左右兩個數列中，再各任意挑選一個數作為基準點，重複前述調整方法。反覆直到基準點左右無法分出新的數列為止，即完成排序。
  
Heap Sort
----
- 一個堆(Heap)的結構:  
1.會是一個二元樹(Binary tree)，每一個子樹中的父節點的值必須大於它的兩個子節點。  
2.節點生成方式一定為由上往下，由左往右。  
3.當前節點位置為i時，它的父節點位置就會是(i-1)/2整除部分的位置。  
4.當前節點位置為i時，它的兩個子節點(c1與c2)位置分別會是2i+1, 2i+2。   
  
- Heapify的概念:  
將一個節點作為父節點出發，若父節點沒有比它的子節點大，則將較大的子節點跟父節點做交換，  
接著再對交換過的子節點再做Heapify，直到當前的節點(位置為i)已經沒有子節點(2i+1已經大於數列長度n)。  
  
- Build Heap建構一個結構正確的堆:   
因為前述的Heapify的特點，若要數列中所有數字都符合Heap的結構，需要再經過整理。  
從最後一個節點的父節點開始往前依次做Heapify，才能確保所有節點都經過整理。  
在建完一個堆之後，才能作Heap Sort。    
  
- Heapsort 堆排序概念:  
將最前面的根節點與樹中最後一個節點作交換，再將最後一個節點排到新的數列中。  
此時最小的數會在根節點位置，不符合Heap結構，所以再從這個節點作一次Heapify，最大值將會再次在節點的位置。  
依此循環，直到所有數都排序好，即完成Heapsort。  
  
Merge Sort
----  
- Merge 合併概念:  
將兩個已排序好的數列A、B合併成新的數列C。  
   
合併方法:  
從AB兩數列分別的第一位數字開始比較，  
若A[0]<B[0]，則將A[0]放進C。接著比較A數列的第二個數跟B數列的第一個數;  
若B[0]<A[0]，則將B[0]放進C。接著比較A數列的第一個數跟B數列的第二個數。  
->以此往下做比較，將當前比較的數，值較小的放在C數列。  
有較小值的數列，其比較位數往後移一位，再與另一數列的數字做比較。  
直到有一邊的數列沒有下一個數了，剩下的數字可以直接放入C數列中(因為兩數列自身已經排序過)，完成合併。  
  
- 拆分概念:  
將一個完整的數列，從中間拆成左右兩個數列，再將拆好的數列分別再次分為左右兩個數列，  
以此循環直到每個數列都只剩下一個數。  
  
- Merge Sort: 先拆分，再合併   
先將要排序的數列，拆分成多個長度為一的數列，再將數列兩兩合併，  
合併完的數列再兩兩合併，直到全部合併為一個數列，即完成Merge Sort。  
  
---
# Week 8
Binary Tree
----
- Binary Tree介紹:  
二元樹是每個節點最多有兩個子樹的樹結構，子樹有左右之分，二元樹常被用於實現二元搜尋樹(binary search tree)和二元堆(binary heap)。  
  
- 參考資料: [二元樹](https://emn178.pixnet.net/blog/post/94164966)
  
---
# Week 9
Binary Search Tree  
----
- Binary Search Tree介紹:   
二元搜尋樹它有以下特性。  
1.在左子樹的鍵值均小於樹根的鍵值。  
2.在右子樹的所有鍵值均大於樹根的鍵值。  
3.左子樹和右子樹亦是二元搜尋樹。  
4.每個鍵值都不一樣。  
  
在BST中的操作，不論是Insert(新增資料)或是Delete(刪除資料)，皆需要先做Search(搜尋)，  
而Search(搜尋)的效率，取決於BST的height(樹高)，如果一棵樹越矮、越平衡(balanced)，則在此BST中搜尋資料的速度較快，  
理想狀況為Complete Binary Tree(時間複雜度：O(logN))。  
反之，若由於輸入資料的順序使得BST沒長好、偏一邊，則在此BST中搜尋資料的最壞情況將有可能如同在Linked List做搜尋(時間複雜度：O(N))。 
 
- 參考資料: [樹狀結構與二元樹](http://marklin-blog.logdown.com/posts/1526463)  



---
# Week 10  
Red Black Tree
----
- Red Black Tree介紹:  
  
- 參考資料: [Red Black Tree: Intro](https://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html)
