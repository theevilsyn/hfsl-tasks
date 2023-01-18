# Web Tasks

### What is DOM?

  - It s a programming interface for HTML and XML documents.
    - It represents the structure of a document as a tree-like structure.
    - Each element of the document (such as a paragraph, image, or form) represented as a node in the tree.
  - It allows developers to access, modify, and manipulate the content, structure, and style of a document using JavaScript or other programming languages.
    - This allows for dynamic updates to the web page, user interaction, and other dynamic behaviors.

### How to get a DOM element using JS?

There are several ways to get a DOM element using JavaScript:
    
      1.  `document.getElementById()`
      2.  `document.getElementsByClassName()`
      3.  `document.getElementsByTagName()`
      4.  `document.querySelector()`
      5.  `document.querySelectorAll()`

1. document.getElementById() -> returns a single element with the given id. For example, if you have an element with an id of "element-1", the following code to get the element: 
`var myElement = document.getElementById("element-1");`
2. document.getElementsByClassName() -> returns a collection of elements with the given class name. For example, if you have an element with a class of "element-1", the following code to get the element:
`var myElements = document.getElementsByClassName("element-1");`
3. document.getElementsByTagName() -> returns a list of elements with the given tag name. For example, if you want to get all the `<p>` elements on the page, you can use the following code: 
`var paragraphs = document.getElementsByTagName("p");`
4. document.querySelector() -> returns the first element that matches a CSS selector. For example, if you have a class of `"my-class"` on an element, you can use the following code to get the element:
`var myElement = document.querySelector(".my-class");`
5. document.querySelectorAll() -> returns a list of elements that match a CSS selector. For example, if you have a class of `"my-class"` on an element, you can use the following code to get the element:
`var myElements = document.querySelectorAll(".my-class");`

All these methods return a reference to the element or a list of elements. You can then use the reference to access the element's properties and methods. Moreover, it returns the first element that matches the specified criteria or an empty list if there is no match.

### If you know handlebars, what is the difference between {{body}} and {{{body}}}?

1.   `{{body}}` -> This will escape the body content. It will replace the special characters with HTML entities. For example, `<` will be replaced with `&lt;`.
    
2.  `{{{body}}}` -> This will not escape the body content. It will render the body content as it is. For example, `<` will be rendered as `<`.

For example, if you have the following content in the body:
    
    <p>This is a paragraph</p>
    <p>This is another paragraph</p>

If you use `{{body}}`, the content will be rendered as:
        
        &lt;p&gt;This is a paragraph&lt;/p&gt;
        &lt;p&gt;This is another paragraph&lt;/p&gt;

If you use `{{{body}}}`, the content will be rendered as:
        
        <p>This is a paragraph</p>
        <p>This is another paragraph</p>




