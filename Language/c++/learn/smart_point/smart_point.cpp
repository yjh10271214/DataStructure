#include<iostream>
#include<memory>

int main() {
    //独占指针，唯一的指向一块资源,不允许拷贝保证唯一性，可以资源转移
    std::unique_ptr<int[], std::default_delete<int[]>> sp1(new int[10]); 
    std::unique_ptr<int[]> sp2(std::move(sp1));

    //共享指针，可以多个对象指向一块资源，还包含一个计数器，为0才会析构
    std::shared_ptr<int[]> sp3(new int[10], std::default_delete<int[]>());
    std::cout << sp3.use_count() << std::endl;
    std::shared_ptr<int[]> sp4(sp3);
    std::cout << sp3.use_count() << std::endl;
    std::shared_ptr<int[]> sp5(sp4);
    std::cout << sp3.use_count() << std::endl;
    std::cout << sp3.get() << std::endl;
    auto sp6 = std::make_shared<int[]>(4);
    std::cout << sp6.use_count() << std::endl;
    std::cout << sp6.get() << std::endl;

    return 0;
}

