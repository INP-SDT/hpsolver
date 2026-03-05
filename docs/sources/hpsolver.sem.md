<!--
{
  "webtitle": "Modules \u2014 hpsolver documentation",
  "codeblocks": false
}
-->

# hpsolver.sem

Spectral element solver.

## newroot()

<pre class="py-sign">hpsolver.sem.<b>newroot</b>(x_1, x_2)</pre>

Creates new HPS root.

<b>Parameters</b>

<p><span class="vardef"><code>x_1</code> : <em>float</em></span></p>

<dl><dd>
  West endpoint of the interval.
</dd></dl>

<p><span class="vardef"><code>x_2</code> : <em>float</em></span></p>

<dl><dd>
  East endpoint of the interval.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

## HPSRoot

<pre class="py-sign"><b><em>class</em></b> hpsolver.sem.<b>HPSRoot</b>(rank)</pre>

Root of the HPS tree.

<b>Properties</b>

Name   | Decription
-------|--------------------------------------
`u_1`  | Solution value at the west endpoint.
`u_2`  | Solution value at the east endpoint.

### reset()

<pre class="py-sign">HPSRoot.<b>reset</b>(<em>self</em>)</pre>

Deactivates the tree after computation.

### activate()

<pre class="py-sign">HPSRoot.<b>activate</b>(<em>self</em>, order) → <em>None</em></pre>

Activates the tree for computation.

<b>Parameters</b>

<p><span class="vardef"><code>order</code> : <em>int</em></span></p>

<dl><dd>
  Order of the scheme (2-6).
</dd></dl>

### setcoeffs()

<pre class="py-sign">HPSRoot.<b>setcoeffs</b>(<em>self</em>, data)</pre>

Defines the equation coefficients.

<b>Parameters</b>

<p><span class="vardef"><code>data</code> : <em>dict</em></span></p>

<dl><dd>
  Provides equation coefficients as lists.
</dd></dl>

### build_operator()

<pre class="py-sign">HPSRoot.<b>build_operator</b>(<em>self</em>) → <em>None</em></pre>

Builds the solution operator.

### build_solution()

<pre class="py-sign">HPSRoot.<b>build_solution</b>(<em>self</em>) → <em>None</em></pre>

Builds the solution after boundary conditions are applied.

### dtn_mat()

<pre class="py-sign">HPSRoot.<b>dtn_mat</b>(<em>self</em>)</pre>

Returns the matrix of the DtN operator.

### dtn_vec()

<pre class="py-sign">HPSRoot.<b>dtn_vec</b>(<em>self</em>)</pre>

Returns the vector of the DtN operator.

### vmesh()

<pre class="py-sign">HPSRoot.<b>vmesh</b>(<em>self</em>)</pre>

Retrieves mesh elements and stacks them vertically.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>2d-array</em></span></p>

<dl><dd>
  Mesh as a vertical stack of elements.
</dd></dl>

### hmesh()

<pre class="py-sign">HPSRoot.<b>hmesh</b>(<em>self</em>)</pre>

Retrieves mesh elements and stacks them horizontally.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-array</em></span></p>

<dl><dd>
  Mesh as a horizontal stack of elements.
</dd></dl>

### vdata()

<pre class="py-sign">HPSRoot.<b>vdata</b>(<em>self</em>)</pre>

Retrieves data from elements and stacks them vertically.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>2d-array</em></span></p>

<dl><dd>
  Data from elements stacked vertically.
</dd></dl>

### hdata()

<pre class="py-sign">HPSRoot.<b>hdata</b>(<em>self</em>)</pre>

Retrieves data from elements and stacks them horizontally.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-array</em></span></p>

<dl><dd>
  Data from elements stacked horizontally.
</dd></dl>

### vgrad()

<pre class="py-sign">HPSRoot.<b>vgrad</b>(<em>self</em>)</pre>

Retrieves gradient from elements and stacks it vertically.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>2d-array</em></span></p>

<dl><dd>
  Gradient from elements stacked vertically.
</dd></dl>

### hgrad()

<pre class="py-sign">HPSRoot.<b>hgrad</b>(<em>self</em>)</pre>

Retrieves data from elements and stacks it horizontally.

<b>Parameters</b>

<p><span class="vardef"><code>root</code> : <em>HPSNode</em></span></p>

<dl><dd>
  Root of the HPS tree.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-array</em></span></p>

<dl><dd>
  Gradient from elements stacked horizontally.
</dd></dl>