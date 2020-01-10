HW 4
====

Hash Table  
----
- Hash Table介紹:  
在用雜湊函數運算出來的雜湊值，根據鍵 (key) 來儲存在數據結構中。而存放這些記錄的數組就稱為雜湊表。  
每筆資料能運算出獨一無二的雜湊值，利用取餘數的方法來決定要儲存在哪以個位置。    
    
- Collision(碰撞)  
若新增新的資料時產生碰撞，代表使用雜湊函數後得出的雜湊值並非唯一，這樣會發生前一筆資料被後一筆資料覆蓋過去的問題。  
此時解決方法，Chaining：使用Linked list把「Hashing到同一個slot」的資料串起來。   
    
- Insert  
1.將資料的雜湊值運算出來。  
2.放進array index為該值的linked list中。  
3.時間複雜度:O(1)   
    
- Delete   
1.將資料的雜湊值運算出來。    
2.利用Linked list的traversal尋找該值。    
    
- Search    
1.將資料的雜湊值運算出來。    
2.利用Linked list的traversal尋找該值。    
3.將節點重新連接。     
    
- Search與Delete的時間複雜度：    
worst case：O(n)，所有資料都被分配到同一個slot中。  
average case：O(1+α)，其中α=「資料數量(n)」除以「slot個數(m)」。    
  
- 參考資料: 1.[資料結構-雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)   2.[Hash Table：Intro](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#ht)   3.[Hash Table：Chaining](http://alrightchiu.github.io/SecondRound/hash-tablechaining.html)  
