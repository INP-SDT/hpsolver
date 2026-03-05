<!--
{
  "webtitle": "Modules \u2014 hpsolver documentation",
  "codeblocks": false
}
-->

# hpsolver.hps

HPS binary tree.

## newgeom()

<pre class="py-sign">hpsolver.hps.<b>newgeom</b>(x_1, x_2)</pre>

Creates a new HPS node with HPS-Geometry data.

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
  HPS node with HPS-Geometry data.
</dd></dl>

## newpsn()

<pre class="py-sign">hpsolver.hps.<b>newpsn</b>(x_1, x_2)</pre>

Creates a new HPS node with HPS-Poisson data.

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
  HPS node with HPS-Poisson data.
</dd></dl>

## HPSNode

<pre class="py-sign"><b><em>class</em></b> hpsolver.hps.<b>HPSNode</b>(rank)</pre>

1D HPS node.

### add_nodes()

<pre class="py-sign">HPSNode.<b>add_nodes</b>(<em>self</em>, mask=<span>None</span>)</pre>

Adds nodes to the unit.

<b>Parameters</b>

<p><span class="vardef"><code>mask</code> : <em>Callable = None</em></span></p>

<dl><dd>
  Boolean predicate that selects the nodes to expand (a).
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>self</em></span></p>

<dl><dd>
  Node itself.
</dd></dl>

<b>Notes</b>

(a) By default, all leaf nodes are expanded.

### del_nodes()

<pre class="py-sign">HPSNode.<b>del_nodes</b>(<em>self</em>, mask=<span>None</span>)</pre>

Removes nodes from the unit.

<b>Parameters</b>

<p><span class="vardef"><code>mask</code> : <em>Callable = None</em></span></p>

<dl><dd>
  Boolean predicate that selects the nodes to delete (a).
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>self</em></span></p>

<dl><dd>
  Node itself.
</dd></dl>

<b>Notes</b>

(a) By default, all leaf nodes are deleted.

### get_nodes()

<pre class="py-sign">HPSNode.<b>get_nodes</b>(<em>self</em>, postproc=<span>None</span>)</pre>

Fetches leaf nodes from the unit.

<b>Parameters</b>

<p><span class="vardef"><code>postproc</code> : <em>Callable = None</em></span></p>

<dl><dd>
  Post-processor of the nodes.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>list</em></span></p>

<dl><dd>
  Fetched nodes.
</dd></dl>

### set_nodes()

<pre class="py-sign">HPSNode.<b>set_nodes</b>(<em>self</em>, bank)</pre>

Sets data on the leaf nodes.

<b>Parameters</b>

<p><span class="vardef"><code>bank</code> : <em>Callable | Iterable</em></span></p>

<dl><dd>
  Data on leaf nodes as a function or stack.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>self</em></span></p>

<dl><dd>
  Node itself.
</dd></dl>

### run_nodes()

<pre class="py-sign">HPSNode.<b>run_nodes</b>(<em>self</em>, method_name, *args, **kwargs)</pre>

Runs a method on the data of leaf nodes.

<b>Parameters</b>

<p><span class="vardef"><code>method_name</code> : <em>str</em></span></p>

<dl><dd>
  Name of the method.
</dd></dl>

<p><span class="vardef"><code>args</code> : <em>tuple</em></span></p>

<dl><dd>
  Positional arguments of the method.
</dd></dl>

<p><span class="vardef"><code>kwargs</code> : <em>dict</em></span></p>

<dl><dd>
  Keyword arguments of the method.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>self</em></span></p>

<dl><dd>
  Node itself.
</dd></dl>

### get_tree()

<pre class="py-sign">HPSNode.<b>get_tree</b>(<em>self</em>) → <em>list</em></pre>

Returns all nodes of the tree as a list.

### make_sol()

<pre class="py-sign">HPSNode.<b>make_sol</b>(<em>self</em>)</pre>

Computes the global solution.

### make_opr()

<pre class="py-sign">HPSNode.<b>make_opr</b>(<em>self</em>)</pre>

Builds the global solution operator.

### make_dtn_leaf()

<pre class="py-sign">HPSNode.<b>make_dtn_leaf</b>(<em>self</em>)</pre>

Builds the DtN operators on leaf nodes.

### make_sol_leaf()

<pre class="py-sign">HPSNode.<b>make_sol_leaf</b>(<em>self</em>)</pre>

Builds the solution on leaf nodes.

## HPSData

<pre class="py-sign"><b><em>class</em></b> hpsolver.hps.<b>HPSData</b>(x_1, x_2, body=<span>None</span>)</pre>

ABC for HPS-Data.

<b>Attributes</b>

<p><span class="vardef"><code>body</code> : <em>matrix-like</em></span></p>

<dl><dd>
  Raw data on the HPS node.
</dd></dl>

<b>Properties</b>

Name       | Description
-----------|--------------------------------------
`x12`      | Interval as a tuple.
`d_x`      | Width of the interval.
`u_1`      | West value of the solition.
`u_2`      | East value of the solition.

### new_body_west()

<pre class="py-sign">HPSData.<b>new_body_west</b>(<em>self</em>)</pre>

Creates the new body for the west children.

<b>Returns</b>

<p><span class="vardef"><em>matrix-like</em></span></p>

<dl><dd>
  New body of the west children.
</dd></dl>

### new_body_east()

<pre class="py-sign">HPSData.<b>new_body_east</b>(<em>self</em>)</pre>

Creates the new body for the east children.

<b>Returns</b>

<p><span class="vardef"><em>matrix-like</em></span></p>

<dl><dd>
  New body of the east children.
</dd></dl>

### new_body_join()

<pre class="py-sign">HPSData.<b>new_body_join</b>(<em>self</em>, west_data, east_data)</pre>

Creates the new body from the children data.

<b>Returns</b>

<p><span class="vardef"><em>matrix-like</em></span></p>

<dl><dd>
  New body merged from the children data.
</dd></dl>

### mat_from_body()

<pre class="py-sign">HPSData.<b>mat_from_body</b>(<em>self</em>) → <em>dict</em></pre>

Makes the DtN matrix from a body.

<b>Returns</b>

<p><span class="vardef"><em>dict</em></span></p>

<dl><dd>
  Matrix entries as arrays.
</dd></dl>

<b>Notes</b>

Keys must be `a11`, `a12`, `a21`, `a22`.

### vec_from_body()

<pre class="py-sign">HPSData.<b>vec_from_body</b>(<em>self</em>) → <em>dict</em></pre>

Makes the DtN vector from a body.

<b>Returns</b>

<p><span class="vardef"><em>dict</em></span></p>

<dl><dd>
  Vector entries as arrays.
</dd></dl>

<b>Notes</b>

Keys must be `b_1`, `b_2`.

### make_sol()

<pre class="py-sign">HPSData.<b>make_sol</b>(<em>self</em>) → <em>None</em></pre>

Transfer the solution from the DtN operator to the body.

<b>Notes</b>

Transfers `u_1` and `u_2` to the body.

## HPSGeom

<pre class="py-sign"><b><em>class</em></b> hpsolver.hps.<b>HPSGeom</b>(x_1, x_2, body=<span>None</span>)</pre>

HPS-Geometry data.

- Derived from `HPSData`.
- Contains no body.

## HPSPoisson

<pre class="py-sign"><b><em>class</em></b> hpsolver.hps.<b>HPSPoisson</b>(x_1, x_2, body=<span>None</span>)</pre>

HPS-Poisson data.

- Derived from `HPSData`.
- Implements P1-FEM for the Poisson equation.

<b>Attributes</b>

<p><span class="vardef"><code>body</code> : <em>2x2-float-matrix.</em></span></p>

<dl><dd>
  Potential and density stored row-by-row.
</dd></dl>

<b>Notes</b>

Operator used:

```
Uxx = Rho
```

with `U` being the potential and `Rho` being the density.