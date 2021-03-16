import json

def gen_bin_tree(height, root):

    tree = {str(root): []}

    if height == 1:
        return tree

    left_leaf = root * 2
    right_leaf = root + 2

    height -= 1
    tree[str(root)] = [
        gen_bin_tree(height, left_leaf),
        gen_bin_tree(height, right_leaf)
    ]
    return tree

def main():
    h = int(input("height = "))
    r = int(input("root = "))

    result = gen_bin_tree(height=h, root=r)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()