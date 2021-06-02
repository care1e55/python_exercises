import sys
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def action(self):
        pass

    def __repr__(self) -> str:
        return self.action()


class ProductBuilder(ABC):
    @abstractmethod
    def build_product(self):
        pass


class ProductBuilder_1(ProductBuilder):
    def build_product(self):
        return Product_1()


class ProductBuilder_2(ProductBuilder):
    def build_product(self):
        return Product_2()


class Product_1(Product):
    def action(self) -> str:
        return f'{self.__class__.__name__} action performed'


class Product_2(Product):
    def action(self) -> str:
        return f'{self.__class__.__name__} action performed'


def make_product(builder: ProductBuilder):
    print(builder.build_product())


if __name__ == '__main__':
    if sys.argv[1] == '1':
        make_product(ProductBuilder_1())
    elif sys.argv[1] == '2':
        make_product(ProductBuilder_2())
    else:
        raise ValueError("Invalid option")




