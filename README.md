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
- Week 4 :  
[Insertion Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%204/Insertion%20Sort.py)
. [HW1-Quick Sort](https://github.com/starfish8681/starfish8681/blob/master/HW1/Quicksort_04122105.ipynb)
- Week 6 :  
[Quick Sort_Recursive.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Quick%20Sort_Recursive.py)
. [Heap Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Heap%20Sort.py)
. [Merge Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%206/Merge%20Sort.py)
- Week 8 :  
[Binary Tree_Linked Structure.py](https://github.com/starfish8681/starfish8681/blob/master/Week%208/Binary%20Tree_Linked%20Structure.py)

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
# Week6  
Quick Sort  
----
- Quick Sort介紹:  
在數列中任意挑選一個數作為基準點，然後調整數列，使得基準點左邊的數都比基準點小，右邊的數都比基準點大，此時基準點本身已經排列在正確位置。  
再來，從原基準點左右兩個數列中，再各任意挑選一個數作為基準點，重複前述調整方法。反覆直到基準點左右無法分出新的數列為止，即完成排序。
