## Functions

To declare a function, we use the function keyword and then name the function and it parameters.

```javascript
function example(param1, param2) { // Use curly brackets around the code inside the function
    // code goes here (end each line with semicolon)
}
```

## Events

`onmouseover` - When the user mouses over the element

`onmouseout` - When the user moves their mouse off the element

`onclick` - When the user clicks on the element

## Changing properties

You can access any CSS properties using JavaScript with the following syntax:

```javascript
<element>.style.<property> = "<value>";
// The same as <property>: <value>; with CSS
```

### Examples

- Changing the visibility of an element

```javascript
<element>.style.display = "block";
// Gets the element and sets the display to block (the same as 'display: block;' with CSS)
```

```javascript
<element>.style.display = "none";
// Gets the element and sets the display to none (the same as 'display: none;' with CSS)
```

- Changing the size of an element

```javascript
<element>.style.width = '150px';
<element>.style.height = '150px';
// Sets the width and height of the element to 150px
```

- Changing the colour of an element

```javascript
<element>.style.color = "red";
// Changes the color of the element to red
```

## Selecting elements

Selecting using `this`:

```javascript
this.style.<property> = "<value>";
// Sets the property of the element this line was placed in
```

Selecting using IDs:

```javascript
document.getElementById("text").style.<property> = "<value>";
// Sets the property of the element with the 'text' ID
```

### Examples

```html
<p onclick="this.style.color='red'">Sample text</p>
<!-- Changes the colour of the text to red when the user clicks on it -->
```

```html
<p onmouseover="document.getElementById('text').style.color='red'">Sample text 1</p>
<p id="text">Sample text 2</p>
<!-- Changes the colour of 'Sample text 2' to red when the user clicks on 'Sample text 1' -->
```
