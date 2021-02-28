HTML:

```html
<nav>
  <ul>
    <!-- List entry for each part of the nav bar -->
    <li><a href="index.html">Home</a></li>
    <li><a href="sport.html">Sport</a></li>
    <li><a href="music.html">Music</a></li>
    <li><a href="study.html">Study</a></li>
    <li><a href="drama.html">Drama</a></li>
  </ul>
</nav>
```

CSS:

```css
nav {
  display: block;
  clear: both;
}
nav ul {
  list-style-type: none; /* Removes the bullet points from each item on the list */
}
nav ul li {
  float: left; /* Makes each item of the list next to each other instead of on top */
  width: 100px; /* Adds space between each part of the nav bar */
  text-align: center; /* Makes each part of the nav bar centered */
}
```

Result:

![](images/navbar.png)


You can also add the following to change the colour when you hover over a part of the nav bar:

```css
nav ul li a:hover {
  background-color: red;
}
```

Which will produce this result:

![](images/hover.png)