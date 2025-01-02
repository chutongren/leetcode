数组：
数组在内存中的存储方式: 数组是存放在连续内存空间（所以在删/增添元素的时候，要移动其他元素的地址）上的相同类型数据的集合。
数组可以方便的通过下标索引的方式获取到下标对应的数据。（从0开始）
二维数组在内存的空间地址是连续的么？ 对于C++语言，是的。对于Java，否。



link
连续内存空间：数组需要连续的内存，链表不需要，因为它会指向下一个节点。
内存空间大小：链表节点 ListNode还需要一份空间保存指针（引用），因此链表比数组占用更多的内存空间
python代码：首先 初始化各个节点，然后 构建节点之间的引用。
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n0.next = n1
n1.next = n2
链表插入节点：空间复杂度O(1)，拉踩数组O(n)，所有后面的都要往后移动一位
P.next = n1
n0.next = P
链表删除节点：n0.next = n1
访问节点效率低，tmd得从第一个开始报数，时间复杂度O(n)，拉踩数组O(1)




广度优先遍历breadth-first traversal
深度 depth-first 先走到尽头，再回溯继续


# 1071. 字符串的最大公因子
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # WHY range(min(len(str1), len(str2)),0, 1)), NOT START FROM 1
        # [) range(), array[]
        # 从，长度上的最大值，开始
        for i in range(min(len(str1), len(str2)),0, -1): 
            # 长度上也要既能除尽它，又能除尽它
            # 是%，不是//，%看能否除尽，是不是整数倍，长度是不是整数倍
            if(len(str1) % i == 0 and len(str2) % i == 0):
            # 取数  重复个数/次数
            # 想法先取str1各部分试，再str2，但最后要找的x如果在str2存在，str1必存在
            # x的开始是固定的，一定是str1的第一个
            # so，这道题重点就是长度上的要求，然后从str1的index=0开始取就完事
                if(str1[:i] * (len(str1)//i) == str1 and str1[:i] * (len(str2)//i) == str2): # 每次对两个字符串做拼接和比较，耗时 O(len1 + len2)
                    return str1[:i]
        return ''

# 1207. 独一无二的出现次数
# 每个数的出现次数都是独一无二的，而不是 每个数都是独一无二的
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = Counter(arr).values() # count
        return len(set(num)) == len(num) # set去掉了重复的元素后，长度还是不变，说明无重复

跟随代码随想录的顺序
暴力解法就是比如双层for循环，时间复杂度O(n2)，



一．数组
# 704 二分查找注意边界条件，左闭右闭边界减一加一，循环中更新left，right和mid
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1;
        int mid=0;
        while(l<=r){
            mid = l + (r-l)/2;
            if(nums[mid]<target){
                l = mid+1;
            }
            else if(nums[mid]>target){
                r = mid-1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
};

# 27. Remove Element 移除元素（删）
快慢指针（不用真的定义ListNode，而是双指针的思想，定义的是i和j就好，都从下标index=0的位置开始）

# Solution 1, double loop
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]==val){
                for(int j=i;j<n-1;j++){
                    nums[j]=nums[j+1];
                }
                i--; /*非常重要的一句话！i位置是val，后面的全都提前一位覆盖，这没错。但是！如果覆盖后的i位置还是val，那就检测不到了（因为i++，已经往下走了）*/
                n--;
            }
        }
        return n;
    }
}; 
# Solution 2, double pointer双指针法
# 快指针快速往下走，过一遍，看哪些值是要的（除了要删的值之外），慢指针慢慢把要的值保存下来（下标在走，然后存值）
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slowIndex=0, n=nums.size();
        for(int fastIndex=0; fastIndex<n; fastIndex++){
            if(nums[fastIndex]!=val){
                nums[slowIndex] = nums[fastIndex]; //赋值
                slowIndex++; //下标在走
            }
        }
        return slowIndex;
    }
};

# 977. Squares of a Sorted Array 有序数组的平方 （含负数）
双指针，谁大谁先被存进去
# 注意i,j,k的值代表啥，注意初始值，使用的时候，怎么改变它
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 0); //长度为n，初始化值为0，vector当数组用
        int i = 0, j = n-1; //两端
        int k = n-1; 

        while(i<=j){
            if(nums[i]*nums[i]>nums[j]*nums[j]){
                result[k]=nums[i]*nums[i];
                i++;
            }
            else{
                result[k]=nums[j]*nums[j];
                j--;
            }
            k--;
        }
        return result;
    }
};
这两道题总结：双指针可以做到，在全局比较中，选择要的元素存入新数组

209.长度最小的子数组
数值加起来不超过target
滑动窗口用一个for解决两个for能做到的事，就是不断的调节子序列的起始位置i和终止位置j，从而得出我们要想的结果。先确定终止位置j，确定sum>target，再动态移动起始位置i，找最小长度
???? 还是不是很理解，start = i,
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0, n=nums.size(), result = INT32_MAX, sum=0;  
# result = INT32_MAX是为了应付你case3测试用例情况：输入：target = 11, nums = [1,1,1,1,1,1,1,1]  输出：0（此时result=8小于target，完全没有进入while循环，所以返回的不能是result初始值，而应该是0。总之result初始值设置为无穷大，只是为了记录是否进入过循环（所有数值加起来都超不过target），若无，则返回0即可
        for (int j=0;j<n;j++){
            sum += nums[j];        /*怎么求sum*/
            while(sum>=target){  //sum大于target了，再确定起始位置i
                int start = i, end = j;
                int temp = j-i+1;    //因为这道题只需要知道长度大小，不需要给出具体nums[i]
                result = result > temp ? temp : result;              
                sum -=nums[i];
                i++;
            }
        }
        return result == INT32_MAX ? 0 : result;
    }
};

0059.螺旋矩阵II
传统的二维数组如 int arr[n][n] 的大小必须在编译时确定。使用 vector 可以在运行时定义数组的大小，可变大小，动态分配内存和释放内存new/delete。可使用push_back、resize等函数。
vector<vector<int>> res(n, vector<int>(m, 0)); 会创建一个 n 行 m 列的二维数组，初始值为 0。

你首先要知道赋值几圈？答n/2圈
每一圈就是4个for循环，分别赋值四条边，注意每条边赋值都是左闭又开，这样才不会打架（重复赋值）。只用offset一个变量即可（代码随想录里面有startx和starty两个变量，只是便于理解，不是必需品
最后，如果n是奇数，那么中间元素还需要赋值为n的平方

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n,vector<int>(n,0));
        int count=1, loop=n/2;
        int offset=0;
        while(loop--){
            int i=0,j=0;
            for(j=offset;j<n-1-offset;j++){
                res[i+offset][j]=count++;
            }
            for(i=offset;i<n-1-offset;i++){
                res[i][j]=count++;
            }
            for(j=n-offset-1;j>offset;j--){
                res[n-1-offset][j]=count++;
            }
            for(i=n-offset-1;i>offset;i--){
                res[i][offset]=count++;
            }
            offset++;
// 这里有一行空格，runtime就是0ms；没有就是2ms。奇怪
        }
        if(n%2==1){res[n/2][n/2]=n*n;}
        return res;
    }
};



二．链表
链表会走路，指针可以走，cur=cur->next
如果要创建一个节点空间，才ListNode* cur= new ListNode(0); //分配空间
如果要删除第n个或者倒数第n个节点，善用n到达你想去的位置。while(n--)
虚拟头节点巧妙一致化，不用再单独考虑头节点。
ListNode* dummyHead = new ListNode(0);
dummyHead->next = head;

链表：203.移除链表元素 给下标index（也是从0开始）
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *dummyhead= new ListNode(0); 
        ListNode* cur = dummyhead;
        dummyhead->next = head;
        while(cur->next != NULL){
            if(cur->next->val == val){
                cur->next = cur->next->next; #但运行时间1ms，解决办法: 用一个tmp放要删掉的节点，然后delete掉它，释放内存空间              
ListNode* tmp = cur->next;
                cur->next = cur->next->next;
                delete tmp;
            }else{ # 不是所有情况都执行cur = cur->next; 一定要写在else里面！！！！
                cur = cur->next;
            }
        }
        return dummyhead->next;
    }
};

707.设计链表
注意：cur=dummyhead，而不是cur=dummyhead->next，原因？？？？
class MyLinkedList {
private:
    int _size;
    LinkedNode* _dummyHead;

public:
    // 定义链表节点结构体
    struct LinkedNode {
        int val;
        LinkedNode* next;
        LinkedNode(int val):val(val), next(nullptr){}
    };

    // 初始化链表 有一个虚拟头节点：简化操作逻辑。它的存在使得所有链表操作可以统一处理，而不需要单独处理头结点的特殊情况。
    MyLinkedList() { 
        _dummyHead = new LinkedNode(0); // 这里定义的头结点 是一个虚拟头结点，而不是真正的链表头结点
        _size = 0;
    }

// 获取到第index个节点数值，如果index是非法数值直接返回-1， 注意index是从0开始的，第0个节点就是头结点
//get只是查询，不需要改变size的值（size++或者size--
    int get(int index) {
        if (index > (_size - 1) || index < 0) {
            return -1;
        }
        LinkedNode* cur = _dummyHead->next;
        while(index--){ // 如果--index 就会陷入死循环
            cur = cur->next;
        }
        return cur->val;
    }

    // 在链表最前面插入一个节点，插入完成后，新插入的节点为链表的新的头结点
    void addAtHead(int val) {
        LinkedNode* newNode = new LinkedNode(val);
        newNode->next = _dummyHead->next;
        _dummyHead->next = newNode;
        _size++;
    }

    // 在链表最后面添加一个节点
    void addAtTail(int val) {
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dummyHead;
        while(cur->next != nullptr){
            cur = cur->next;
        }
        cur->next = newNode;
        _size++;
    }

    // 在第index个节点之前插入一个新节点，例如index为0，那么新插入的节点为链表的新头节点。
    // 如果index 等于链表的长度，则说明是新插入的节点为链表的尾结点
    // 如果index大于链表的长度，则返回空
    // 如果index小于0，则在头部插入节点
    void addAtIndex(int index, int val) {

        if(index > _size) return;
        if(index < 0) index = 0;        
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dummyHead;
        while(index--) {
            cur = cur->next;
        }
        newNode->next = cur->next;
        cur->next = newNode;
        _size++;
    }

    // 删除第index个节点，如果index 大于等于链表的长度，直接return，注意index是从0开始的
    void deleteAtIndex(int index) {
        if (index >= _size || index < 0) {
            return;
        }
        LinkedNode* cur = _dummyHead;
        while(index--) {
            cur = cur ->next;
        }
        LinkedNode* tmp = cur->next;
        cur->next = cur->next->next;
        delete tmp;
        //delete命令指示释放了tmp指针原本所指的那部分内存，
        //被delete后的指针tmp的值（地址）并非就是NULL，而是随机值。也就是被delete后，
        //如果不再加上一句tmp=nullptr,tmp会成为乱指的野指针
        //如果之后的程序不小心使用了tmp，会指向难以预想的内存空间
        tmp=nullptr;
        _size--;
    }

    // 打印链表
    void printLinkedList() {
        LinkedNode* cur = _dummyHead;
        while (cur->next != nullptr) {
            cout << cur->next->val << " ";
            cur = cur->next;
        }
        cout << endl;
    }
};
0206.翻转链表
改变指针指向，用一个pre，一个cur
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* pre = NULL;
        while(cur!=NULL){
            ListNode* tmp=cur->next;
            cur->next = pre;
            pre=cur;
            cur=tmp;
        }
        return pre;
    }
};

24. Swap Nodes in Pairs
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* cur = dummyHead;
        while (cur->next != NULL && cur->next->next != NULL) { // 修改条件，避免空指针
            ListNode* tmp = cur->next;
            ListNode* tmp2 = cur->next->next;

            // 调整指针顺序，正确交换节点
            cur->next = tmp2;
            tmp->next = tmp2->next;
            tmp2->next = tmp;

            // 移动cur指针，准备交换下一对
            cur = tmp;
        }
        return dummyHead->next;
    }
};

19.Remove Nth Node From End of List 删除倒数第N个节点
快慢指针
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(n--){
            fast = fast->next;
        }
        if(fast==NULL){
            head = head->next;
        }
        else{
            while(fast->next!=NULL){
                fast=fast->next;
                slow=slow->next;
            }
            slow->next=slow->next->next;
        }
        return head;
    }

};

142. Linked List Cycle II 环形链表
错误1:                ListNode * index1 = new ListNode(0);
                ListNode * index2 = new ListNode(0);
                index1 = head;
                index2 = slow;
index1 和 index2 的初始化可以直接赋值为 head 和 slow，无需创建新节点。//不需要创建一个物理位置给他
错误2：链表的循环终止条件我总是拿不准
while(fast && fast->next) 
因为fast->next可以是最后一个节点，fast->next->next空了进入下一次while就不执行循环了


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode * fast = head;
        ListNode * slow = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast==slow){
                ListNode * index1 = head;
                ListNode * index2 = slow;
                while(index1!=index2){
                    index1=index1->next;
                    index2=index2->next;
                }
                return index1;
            }
        }
        return NULL; //没有环，没找到，那么就返回NULL
    }
};



三．哈希表
0242.有效的字母异位词
class Solution {
public:
    bool isAnagram(string s, string t) {
        // int hash[26]=0;
        int hash[26]={0};
        for(int i=0;i<s.size();i++){
            hash[s[i]-'a']++;
        }
        for(int i=0;i<t.size();i++){
            hash[t[i]-'a']--;
        }
        for(int i=0;i<26;i++){
            if(hash[i]!=0) return false;
        }
        return true;
    }
};
哈希表都是用来快速判断一个元素是否出现集合里。

1. Two Sum
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for(int i=0;i<nums.size();i++){
            auto iter = map.find(target-nums[i]);
            if(iter!=map.end()){
                return {iter->second, i};
            }
            map.insert(pair<int, int>(nums[i],i));
        }
        return {};
    }
};
错误：先for一遍把nums[i]和i存进map。
会造成：if当前 nums[i] 的值是 5，而 target 是 10。此时 target - nums[i] 等于 5。 find(target - nums[i]) 会找到自己。

四．字符串
reverse库函数，时间复杂度是 O(n)，空间复杂度是 O(1)
reverse(start_index, end_index+1) 左闭右开
151.翻转字符串里的单词
class Solution {
public:
    string reverseWords(string s) {
        // Step 1: 去除多余空格
        int slow=0;
        bool exist = false;
        for(int i=0; i<s.size(); i++){
            // i ++ following for loop
            if(s[i]!=' '){
                s[slow++]=s[i];
                exist = true;
                continue;
            }
            if(exist){
                s[slow++] = ' ';
                exist = false;
            }
            // 所以最后如果有空格，那也会变成1个空格，删掉它就好了
        }
        if(s[slow-1]==' '){s.resize(slow-1);}
        else{s.resize(slow);}
        // Step 2: 翻转
        reverse(s.begin(),s.end());
        // Step 3: 再每个单词分别反转
        int start = 0;
        for(int i=0;i<s.size();i++){
            if(s[i]==' '){
                // 如何表示到达string结尾 i==s.size()
                reverse(s.begin()+start,s.begin()+i);
                // reverse(s.begin() + start, (i == s.size() - 1) ? s.begin() + i + 1 : s.begin() + i);
                start = i+1;
            }
            if(i==s.size()-1){
                reverse(s.begin()+start, s.begin()+i+1);
            }
        }
        return s;
    }
};

栈与队列
232.用栈实现队列 Implement Queue using Stacks 
StIn和StOut

20. 有效的括号Valid Parentheses
括号匹配是使用栈解决的经典问题。如果s[i]是左括号，那么就放对应的右括号进stack，else pop，最后stack为空就是有效的括号。
三种情况：
1）左方向括号，数量多余
2）右方向括号，数量多余
3）没有多余，但括号类型不匹配

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                st.push(')');
            }else if(s[i]=='['){
                st.push(']');
            }else if(s[i]=='{'){
                st.push('}');
            }
            //不是左括号就是右括号了 
            //值不相等
            // else if(s[i]!=st.top()||st.empty()){return false;} //RE
            else if(st.empty()||s[i]!=st.top()){return false;} //要先保证st不为空
            else{
                st.pop();
            }
        }
        return st.empty();//左多
    }
};





二叉树

5. 二叉树的层序遍历 102. Binary Tree Level Order Traversal   
队列先进先出，符合一层一层遍历的逻辑。（用栈先进后出适合模拟深度优先遍历也就是递归的逻辑。这种层序遍历方式就是图论中的广度优先遍历，只不过现在我们应用在二叉树上。

两层循环
while(!que.empty()) 	  遍历二叉树的每一层，放进result每一行
for(int i = 0; i < size; i++)  遍历当前层的每一个节点

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // vector<int> que; //取出来，还需要他的左右孩子信息
        queue<TreeNode*> que;
        if(root!=NULL) que.push(root);

        // vector<int> vec;
        vector<vector<int>> result; //result是个二维数组，把每一层的节点存进result的一行
        TreeNode* node;
        
        while(!que.empty()){ //二叉树的每一层，result每一行  这里不是while(size--)!!! 因为size是queue的长度，which动态变化
            int size = que.size();
            vector<int> vec; // 定义在这里，也有清空vec的作用
            for(int i = 0; i < size; i++){//当前层的每一个节点
                node = que.front();//pop之前，赋给一个temp变量
                que.pop();
                vec.push_back(node->val);
                if(node->left) que.push(node->left);
                if(node->right) que.push(node->right);
                // size=que.size();
            }
            result.push_back(vec);
        }
        return result;
    }
};

6.翻转二叉树  226. Invert Binary Tree 
其实就把每一个节点的左右孩子交换一下就可以了。关键在于遍历顺序，前中后序应该选哪一种遍历顺序？答
TreeNode* invertTree(TreeNode* root) {
        if(root==NULL){   //递归的终止条件
            return NULL;
        }
        swap(root->left, root->right); //swap函数是啥？可以直接用诶
        invertTree(root->left);
        invertTree(root->right);
        return root; //递归 就是 函数内调用自己，就是相当于while，终于乱码七糟完事，跳出来了，返回root就好了
}

7.总结

8.对称二叉树  101.
根节点的左子树和右子树是否可以翻转？比较的是左右子树，不是左右子节点
遍历左右子树要比较的是内侧和外侧节点。后序遍历


class Solution {
public:
bool compare(TreeNode* left, TreeNode* right){
// 为空
        if(left==NULL && right==NULL) {return true;}
        if(left!=NULL && right==NULL) {return false;}
        if(left==NULL && right!=NULL) {return false;}
        if(left->val != right->val) {return false;} 
       // 左右非空且相等 就再往里判断
        return compare(left->left,right->right)&&compare(left->right,right->left);//外侧，内侧
    }
    bool isSymmetric(TreeNode* root) {
        if(root==NULL) {return false;}
        return compare(root->left,root->right);
    }
};

9.二叉树的最大深度 ，就是根节点的深度    104. Maximum Depth of Binary Tree
往下钻井叫深度，往上生长叫高度。前序求的是深度，后序求的是高度。
父节点知道子节点的深度，直接加个一就可以了
class Solution {
public:
    int childDepth(TreeNode* node){
        if(node == NULL) return 0;
        int leftDepth = childDepth(node->left);
        int rightDepth = childDepth(node->right);
        return max(leftDepth,rightDepth)+1;
    }
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        return childDepth(root);
    }
};

10.二叉树的最小深度     111.
给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数量。说明: 叶子节点是指没有子节点的节点。




回溯
77.组合
class Solution {
private:
    vector<vector<int>> result; // 存放符合条件结果的集合
    vector<int> path; // 用来存放符合条件结果
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = startIndex; i <= n; i++) {
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1); // 递归
            path.pop_back(); // 回溯，撤销处理的节点
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        result.clear(); // 可以不写
        path.clear();   // 可以不写
        backtracking(n, k, 1);
        return result;
    }
};
216. Combination Sum III     和为n的k个数的集合
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(int k, int n, int startIndex, int sum){
        if(sum==n){
            if(path.size()==k){
                result.push_back(path);
}
                return ;
        }
        // 固定三层
        for(int i =startIndex; i<=9;i++){
            sum+=i;
            path.push_back(i);
            backtracking(k,n,i+1,sum);
            sum-=i;
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        backtracking(k, n, 1, 0);
        return result;
    }
};



# 1071. 字符串的最大公因子
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # WHY range(min(len(str1), len(str2)),0, 1)), NOT START FROM 1
        # [) range(), array[]
        # 从，长度上的最大值，开始
        for i in range(min(len(str1), len(str2)),0, -1): 
            # 长度上也要既能除尽它，又能除尽它
            # 是%，不是//，%看能否除尽，是不是整数倍，长度是不是整数倍
            if(len(str1) % i == 0 and len(str2) % i == 0):
            # 取数  重复个数/次数
            # 想法先取str1各部分试，再str2，但最后要找的x如果在str2存在，str1必存在
            # x的开始是固定的，一定是str1的第一个
            # so，这道题重点就是长度上的要求，然后从str1的index=0开始取就完事
                if(str1[:i] * (len(str1)//i) == str1 and str1[:i] * (len(str2)//i) == str2): # 每次对两个字符串做拼接和比较，耗时 O(len1 + len2)
                    return str1[:i]
        return ''

# 1207. 独一无二的出现次数
# 每个数的出现次数都是独一无二的，而不是 每个数都是独一无二的
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = Counter(arr).values() # count
        return len(set(num)) == len(num) # set去掉了重复的元素后，长度还是不变，说明无重复

# 704 二分查找，循環中更新left，right和mid
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1;
        int mid=0;
        while(l<=r){
            mid = l + (r-l)/2;
            if(nums[mid]<target){
                l = mid+1;
            }
            else if(nums[mid]>target){
                r = mid-1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
};

# 27. Remove Element
# Solution 1, double loop
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]==val){
                for(int j=i;j<n-1;j++){
                    nums[j]=nums[j+1];
                }
                i--; /*非常重要的一句话！i位置是val，后面的全都提前一位覆盖，这没错。但是！如果覆盖后的i位置还是val，那就检测不到了（因为i++，已经往下走了）*/
                n--;
            }
        }
        return n;
    }
}; 
# Solution 2, double pointer双指针法
# 快指针快速往下走，过一遍，看哪些值是要的，慢指针慢慢把要的值保存下来
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slowIndex=0, n=nums.size();
        for(int fastIndex=0; fastIndex<n; fastIndex++){
            if(nums[fastIndex]!=val){
                nums[slowIndex] = nums[fastIndex]; # 赋值
                slowIndex++;
            }
        }
        return slowIndex;
    }
};

# 977. Squares of a Sorted Array 
# 注意i,j,k的值代表啥，注意初始值，使用的时候，怎么改变它
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 0);
        int i = 0, j = n-1;
        int k = n-1;

        while(i<=j){
            if(nums[i]*nums[i]>nums[j]*nums[j]){
                result[k]=nums[i]*nums[i];
                i++;
            }
            else{
                result[k]=nums[j]*nums[j];
                j--;
            }
            k--;
        }
        return result;
    }
};