HW 3
====

Binary Search Tree  
----
- Binary Search Tree介紹:   
二元搜尋樹它有以下特性。  
1.在左子樹的鍵值均小於樹根的鍵值。  
2.在右子樹的所有鍵值均大於樹根的鍵值。  
3.左子樹和右子樹亦是二元搜尋樹。  
4.每個鍵值都不一樣。  
  
在BST中的操作，不論是Insert(新增資料)或是Delete(刪除資料)，皆需要先做Search(搜尋)，  
而Search的效率，取決於height(樹高)，如果一棵樹越矮、越平衡(balanced)，則在此BST中搜尋資料的速度較快，  
理想狀況為Complete Binary Tree(時間複雜度：O(logN))。  
反之，若由於輸入資料的順序使得BST沒長好、偏一邊，則在此BST中搜尋資料的最壞情況將有可能如同在Linked List做搜尋(時間複雜度：O(N))。 
 
