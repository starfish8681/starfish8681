# 資料結構與演算法 學習筆記
04122105 高星瑜

# HW 2
----
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
- Week 3 :  
[Queue.py](https://github.com/starfish8681/starfish8681/blob/master/Week%203/implement-queue-using-stacks.py)
. [Stack,py](https://github.com/starfish8681/starfish8681/blob/master/Week%203/mini%20stack.py)
- Week 4 :  
[Insertion Sort.py](https://github.com/starfish8681/starfish8681/blob/master/Week%204/Insertion%20Sort.py)
. [HW1-Quick Sort](https://github.com/starfish8681/starfish8681/blob/master/%E4%BD%9C%E6%A5%AD/Quicksort_04122105.ipynb)
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
