#https://www.e-olymp.com/uk/submissions/7598731

class AVLNode:
    ''' Вузол AVL-дерева.'''

    def __init__(self, key):
        self.key = key  # Ключ дерева пошуку
        self.parent = None  # Посилання на батька вузла. Якщо вузол є коренем, посилання на об'єкт AVLTree
        self.left = None  # Посилання на лівого сина
        self.right = None  # Посилання на правого сина
        self.balance = 0  # Фактор балансу вузла (від'ємний, якщо дерево перевішує вправо, додатній, якщо вліво)

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_no_children(self):
        return not (self.has_left() or self.has_right())

    def is_root(self):
        return isinstance(self.parent, AVLTree)

    def is_left(self):
        return self is self.parent.left

    def is_right(self):
        return self is self.parent.right

    def is_unbalanced(self):
        return abs(self.balance) > 1

    def set_left(self, key):
        ''' Додає лівого сина. Проводить оновлення балансу'''
        self.left = AVLNode(key)
        self.left.parent = self
        self.left.update_balance()

    def set_right(self, key):
        ''' Додає правого сина. Проводить оновлення балансу'''
        self.right = AVLNode(key)
        self.right.parent = self
        self.right.update_balance()

    def update_balance(self):
        ''' Рекурсивно оновлює баланс вершин від поточного вузла до батька.
        Якщо відбулось розбалансування, запускається процедура перебалансування.
        '''
        if self.is_unbalanced():  # Якщо у вузлі відбулося розбалансування,
            return self.rebalance()  # починаємо процедуру перебалансування
        # Балансування змінює баланс на одиницю у вершині яка розбалансована
        # і, відповідно, у батька баланс уже не зміниться. Тому виконується return.
        # Якщо поточний вузол залишився збалансованим, рекурентно корегуємо баланс предків
        if not self.is_root():  # Якщо дійшли до кореня, балансування завершено
            parent = self.parent
            if self.is_left():  # Якщо поточний вузол є лівим сином, баланс батька збільшується
                parent.balance += 1
            elif self.is_right():  # Якщо поточний вузол є правим сином, баланс батька зменшується
                parent.balance -= 1
            if parent.balance != 0:  # Якщо фактор балансу батька став дорівнювати нулю, балансування завершено,
                parent.update_balance()  # інакше продовжуємо

    def rebalance(self):
        ''' Здійснює балансування дерева у розбалансованій вершині.'''
        if self.balance < 0:
            if self.right.balance > 0:
                self.right.rotate_right()
                self.rotate_left()
            else:
                self.rotate_left()
        elif self.balance > 0:
            if self.left.balance < 0:
                self.left.rotate_left()
                self.rotate_right()
            else:
                self.rotate_right()

    def rotate_left(self):
        ''' Здійснює мале ліве обертання.'''
        parent = self.parent
        if self.is_root():  # Якщо розбалансовано корінь, потрібно встановити на його місце новий
            parent.root = self.__rotate_left()
        elif self.is_left():  # Якщо розбалансовано лівого сина, встановлюємо нового
            parent.left = self.__rotate_left()
        elif self.is_right():  # Якщо розбалансовано правого сина, встановлюємо нового
            parent.right = self.__rotate_left()

    def __rotate_left(self):
        pivot = self.right  # Правий син завжди є, оскільки фактор балансу від'ємний
        self.right = pivot.left

        if pivot.has_left():  # Якщо новий корінь піддерева має лівого сина,
            pivot.left.parent = self  # встановлюємо йому нового батька
        pivot.left = self

        parent = self.parent
        self.parent = pivot  # Старий корінь піддерева стає сином нового кореня піддерева
        pivot.parent = parent  # Батько старого кореня піддерева стає батьком нового кореня піддерева
        # Визначаємо нові фактори балансу згідно формули
        self.balance = self.balance + 1 - min(0, pivot.balance)
        pivot.balance = pivot.balance + 1 + max(0, self.balance)
        # Єдине, що залишилось, встановити відповідне значення для батька pivot
        return pivot  # Повертаємо новий корінь піддерева

    def rotate_right(self):
        ''' Здійснює мале праве обертання.'''
        parent = self.parent
        if self.is_root():
            parent.root = self.__rotate_right()
        elif self.is_left():
            parent.left = self.__rotate_right()
        elif self.is_right():
            parent.right = self.__rotate_right()

    def __rotate_right(self):
        pivot = self.left
        self.left = pivot.right

        if pivot.has_right():
            pivot.right.parent = self
        pivot.right = self

        parent = self.parent
        self.parent = pivot
        pivot.parent = parent

        self.balance = self.balance - 1 - max(0, pivot.balance)
        pivot.balance = pivot.balance - 1 + min(0, self.balance)
        return pivot

    def search(self, key):
        ''' Повертає вузол, якщо вузол з ключем key є в дереві, інакше None.'''
        node = self
        while True:  # Стандартна реалізація нерекурсивного пошуку в дереві пошуку
            if key == node.key:
                return node
            elif key < node.key:
                if node.has_left():
                    node = node.left
                else:
                    break
            else:
                if node.has_right():
                    node = node.right
                else:
                    break

    def search_max(self):
        ''' Повертає вузол з найбільшим елементом в дереві.'''
        node = self
        while node.has_right():
            node = node.right
        return node

    def search_min(self):
        ''' Повертає вузол з найменшим елементом в дереві.'''
        node = self
        while node.has_left():
            node = node.left
        return node

    def update_balance_on_delete(self, came_from_left):
        ''' Після видалення рекурсивно оновлює баланс вершин від поточного вузла до батька.
        Якщо відбулось розбалансування, запускається процедура перебалансування.
        '''
        if came_from_left:  # Якщо прийшли зліва,
            self.balance -= 1  # дерево стає перевішувати вправо
        else:  # Якщо прийшли справа,
            self.balance += 1  # дерево стає перевішувати вліво

        if self.is_unbalanced():
            self.rebalance()
            # Після того, як ми робимо ребаланс, наш вузол від'їзжає назад, а також
            # встановлюється його баланс та баланс його батька за допомогою обертань,
            if not self.is_root():  # Тому батька потрібно перестрибнути
                if self.parent.balance == 0 and not self.parent.is_root():
                    self.parent.parent.update_balance_on_delete(self.parent.is_left())
        # Рекурсивно продовжуємо
        elif self.balance == 0 and not self.is_root():  # Якщо оновлений баланс не дорівнює нулю, це означає, що дерево не зменшилося у висоту
            self.parent.update_balance_on_delete(self.is_left())  # в такому випадку, потрібно потрібно зупинитися

    def delete(self, node_or_key):
        ''' Видаляє вузол з дерева, яки заданий ключем або посиланням,
        якщо такого вузла немає нічго не робить.'''
        if isinstance(node_or_key, AVLNode):  # Шукаємо заданий вузол
            node = node_or_key
        else:
            node = self.search(node_or_key)
        if node is None:  # Якщо такого вузла в дереві немає, нічого не робимо
            return

        parent = node.parent
        if node.has_no_children():  # Якщо знайдений вузол - листок (немає нащадків)
            if node.is_root():  # Якщо вузол єдиний в дереві,
                parent.root = None  # прибираємо на нього посилання
            elif node.is_left():  # Якщо вузол є лівим сином,
                parent.left = None  # прибираємо на нього посилання
                parent.update_balance_on_delete(True)  # Після видалення потрібно оновити баланс
            elif node.is_right():  # Якщо вузол є правим сином,
                parent.right = None  # прибираємо на нього посилання
                parent.update_balance_on_delete(False)  # Після видалення потрібно оновити баланс
        # Якщо знайдений вузол має лише одну ліву гілку, замінюємо знайдений вузол його лівим піддіревом
        elif node.has_left() and not node.has_right():
            if node.is_root():  # Якщо вузол є коренем,
                parent.root = node.left  # встановлюємо новий корінь
                node.left.parent = parent  # Встановлюємо батька для лівого піддерева
                # При цьому балансування проводити не потрібно
            elif node.is_left():  # Якщо вузол є лівим сином,
                parent.left = node.left  # встановлюємо нового нового лівого сина
                node.left.parent = parent  # Встановлюємо батька для лівого піддерева
                parent.update_balance_on_delete(True)  # Після видалення потрібно оновити баланс

            elif node.is_right():  # Якщо вузол є правим сином,
                parent.right = node.left  # встановлюємо нового нового лівого сина
                node.left.parent = parent  # Встановлюємо батька для лівого піддерева
                parent.update_balance_on_delete(False)  # Після видалення потрібно оновити баланс

        # Якщо знайдений вузол має лише одну праву гілку, замінюємо знайдений вузол його правим піддіревом
        elif node.has_right() and not node.has_left():
            if node.is_root():
                parent.root = node.right
                node.right.parent = parent
            elif node.is_left():
                parent.left = node.right
                node.right.parent = parent
                parent.update_balance_on_delete(True)
            elif node.is_right():
                parent.right = node.right
                node.right.parent = parent
                parent.update_balance_on_delete(False)

        else:  # Якщо знайдений вузол має обидві гілки
            left_max = node.left.search_max()  # Знаходимо максимальний вузол у лівому піддереві
            node.key = left_max.key  # Замінюємо значення елемета node знайденим максимальним (якщо у вузлах додатково є навантаженн, потрібно замінити і його)
            node.left.delete(left_max)  # Видаляємо найбільший елемент з лівого піддерева
            # При цьому балансування проводити не вотрібно (воно було проведено в рукерсивному виклиці)

    def exists(self, key):
        ''' Повертає True, якщо вузол з ключем key є в дереві, інакше False.'''
        return bool(self.search(key))

    def insert(self, key):
        ''' Вставляє вузол з ключем key. Якщо він вже є в дереві, нічого не робить.'''
        node = self
        while True:  # Стандартна реалізація нерекурсивної вставки в дерево пошуку
            if key == node.key:
                break
            elif key < node.key:
                if node.has_left():
                    node = node.left
                else:
                    node.set_left(key)
                    break
            else:
                if node.has_right():
                    node = node.right
                else:
                    node.set_right(key)
                    break

    def next(self, key):
        min_el = None
        node = self

        while not node is None:
            if node.key > key:
                min_el = node.key
                node = node.left
            else:
                node = node.right

        return min_el

    def prev(self, key):
        max_el = None
        node = self

        while not node is None:
            if node.key < key:
                max_el = node.key
                node = node.right
            else:
                node = node.left

        return max_el

    def kth(self, k):
        node = self.search_min()
        visited = set()
        k -= 1

        while k > 0:
            visited.add(node.key)

            if node.has_no_children():
                node = node.parent
            elif node.has_left() and not node.has_right() and node.left.key in visited:
                node = node.parent
            elif node.has_right() and not node.has_left() and node.right.key in visited:
                node = node.parent
            elif node.has_left() and node.has_right() and node.left.key in visited and node.right.key in visited:
                node = node.parent
            else:
                if node.has_left() and not node.left.key is visited:
                    node = node.search_min()
                elif node.has_right() and not node.left.key is visited:
                    node = node.right.search_min()

            k -= 1

        if isinstance(node, AVLTree):
            return None
        else:
            return node.key

class AVLTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, key):
        if self.isEmpty():
            self.root = AVLNode(key)
            self.root.parent = self
        else:
            self.root.insert(key)

    def delete(self, key):
        if not self.isEmpty():
            self.root.delete(key)

    def exists(self, key):
        if self.isEmpty():
            return 'false'
        else:
            return 'true' if self.root.exists(key) else 'false'

    def next(self, key):
        if self.isEmpty():
            return 'none'
        else:
            return str(self.root.next(key)).lower()

    def prev(self, key):
        if self.isEmpty():
            return 'none'
        else:
            return str(self.root.prev(key)).lower()

    def kth(self, key):
        if self.isEmpty():
            return 'none'
        else:
            return str(self.root.kth(key)).lower()

    def execute(self, command):
        name, arg = command.split()
        arg = int(arg)

        return getattr(self, name)(arg)

if __name__ == '__main__':
    tree = AVLTree()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            tree = AVLTree()

            for line in input:
                res = tree.execute(line)

                if res:
                    print(res, file=output)
