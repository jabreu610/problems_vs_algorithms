from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_segments, handler, previous_node=None):
        prev = previous_node if previous_node is not None else self.root
        if len(path_segments) == 0:
            prev.handler = handler
            return
        next_seg = path_segments.pop(0)
        curr = prev.children[next_seg]
        self.insert(path_segments, handler, curr)

    def find(self, path_segments, previous_node=None):
        prev = previous_node if previous_node is not None else self.root
        if len(path_segments) > 0 and len(prev.children) == 0:
            return None
        if len(path_segments) == 0:
            return prev.handler
        next_seg = path_segments.pop(0)
        curr = prev.children[next_seg]
        return self.find(path_segments, curr)


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_segments = self.split_path(path)
        self.trie.insert(path_segments, handler)

    def lookup(self, path):
        path_segments = self.split_path(path)
        result = self.trie.find(path_segments)
        return result if result is not None else self.not_found_handler

    def split_path(self, path):
        """Returns path segements for a given path, collapses empty segments created by '//' and trailing slashes"""
        return [x for x in path.split('/') if len(x) > 0]


if __name__ == "__main__":
    def test_case_1():
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about", "about handler")

        print(router.lookup("/"))
        print(router.lookup("/home"))
        print(router.lookup("/home/about"))
        print(router.lookup("/home/about/"))
        print(router.lookup("/home/about/me"))

    def test_case_2():
        router = Router("Udacity home handler", '404: Not Found')
        router.add_handler("/blog", "Udacity blog handler")
        router.add_handler("/blog/2023/01/udacitys-commitment-to-international-day-of-education.html",
                           "Udacity blog post handler: udacitys-commitment-to-international-day-of-education")
        router.add_handler("/blog/2023/01/2023s-fastest-growing-tech-jobs.html",
                           "Udacity blog post handler: 2023s-fastest-growing-tech-jobs")

        print(router.lookup('/'))
        print(router.lookup('/blog'))
        print(router.lookup('//blog'))
        print(router.lookup(
            '/blog/2023/01//udacitys-commitment-to-international-day-of-education.html/'))
        print(router.lookup(
            '/blog/2023/01//udacitys-commitment-to-international-day-of-education.json'))
        print(router.lookup('/blog/2024/01/2023s-fastest-growing-tech-jobs.html'))

    def test_case_3():
        router = Router("200: OK", '404: NOT FOUND')

        print(router.lookup('/'))
        print(router.lookup('////'))
        print(router.lookup('////my-page.html'))
        print(router.lookup('/about/'))
        print(router.lookup(''))
        print(router.lookup('/this/is/a/very/long/path/that/does/not/exist'))

    test_case_1()
    # root handler
    # not found handler
    # about handler
    # about handler
    # not found handler

    print('\n')

    test_case_2()
    # Udacity home handler
    # Udacity blog handler
    # Udacity blog handler
    # Udacity blog post handler: udacitys-commitment-to-international-day-of-education
    # 404: Not Found
    # 404: Not Found

    print('\n')

    test_case_3()
    # 200: OK
    # 200: OK
    # 404: NOT FOUND
    # 404: NOT FOUND
    # 200: OK
    # 404: NOT FOUND
