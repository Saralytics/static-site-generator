class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            props_list = [" " + attr + '="' + value +
                          '"' for attr, value in self.props.items()]
            return "".join(props_list)

        return None

    def __repr__(self):
        html_props = self.props_to_html()
        return f"""HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}). Props are {html_props}"""


class LeafNode(HTMLNode):
    def __init__(self, tag, value, **props) -> None:
        if value is None:
            raise ValueError("Must have value")

        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        attrs = self.props_to_html()
        return f"<{self.tag} {attrs}>{self.value}</{self.tag}>"

    def __repr__(self):
        html_props = self.props_to_html()
        return f"""HTMLNode({self.tag}, {self.value}, {self.props}). Props are {html_props}"""


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list) -> None:
        if tag is None or tag == "":
            raise ValueError("Must provide tag")

        if children is None or len(children) == 0:
            raise ValueError("Must provide children elements")

        super().__init__(tag=tag, children=children)

    def recursive(self, children):
        # base case
        if len(children) == 0:
            return ""

        if children[0].tag is None:
            value = children[0].value
        else:
            value = f"<{children[0].tag}>{
                children[0].value}</{children[0].tag}>"

        return value + self.recursive(children[1:])

    def to_html(self):
        return f"<{self.tag}>{self.recursive(self.children)}</{self.tag}>"

    def __repr__(self):
        html_props = self.props_to_html()
        return f"""HTMLNode({self.tag}, {self.value}, {self.props}). Props are {html_props}"""
