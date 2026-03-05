<!--
{
  "webtitle": "Modules — hpsolver documentation",
  "doctitle": "hpsolver — Modules"
}
-->

## Annotations

Module                | Description             
--------------------- | ------------------------
<b>hpsolver.sem</b>   | Spectral element solver.
<b>hpsolver.hps</b>   | HPS binary tree.        
<b>hpsolver.polys</b> | Polynomial bases.       

## Reference

### hpsolver.sem

<p>
<ul class="ref-list" id="mod-refs">
    <li><a href="hpsolver.sem.md#hpsolver.sem">hpsolver.sem</a>
        <ul>
            <li><a href="hpsolver.sem.md#newroot">newroot()</a></li>
            <li><a href="hpsolver.sem.md#hpsroot">HPSRoot</a>
                <ul>
                    <li><a href="hpsolver.sem.md#reset">reset()</a></li>
                    <li><a href="hpsolver.sem.md#activate">activate()</a></li>
                    <li><a href="hpsolver.sem.md#setcoeffs">setcoeffs()</a></li>
                    <li><a href="hpsolver.sem.md#build_operator">build_operator()</a></li>
                    <li><a href="hpsolver.sem.md#build_solution">build_solution()</a></li>
                    <li><a href="hpsolver.sem.md#dtn_mat">dtn_mat()</a></li>
                    <li><a href="hpsolver.sem.md#dtn_vec">dtn_vec()</a></li>
                    <li><a href="hpsolver.sem.md#vmesh">vmesh()</a></li>
                    <li><a href="hpsolver.sem.md#hmesh">hmesh()</a></li>
                    <li><a href="hpsolver.sem.md#vdata">vdata()</a></li>
                    <li><a href="hpsolver.sem.md#hdata">hdata()</a></li>
                    <li><a href="hpsolver.sem.md#vgrad">vgrad()</a></li>
                    <li><a href="hpsolver.sem.md#hgrad">hgrad()</a></li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
</p>

### hpsolver.hps

<p>
<ul class="ref-list" id="mod-refs">
    <li><a href="hpsolver.hps.md#hpsolver.hps">hpsolver.hps</a>
        <ul>
            <li><a href="hpsolver.hps.md#newgeom">newgeom()</a></li>
            <li><a href="hpsolver.hps.md#newpsn">newpsn()</a></li>
            <li><a href="hpsolver.hps.md#hpsnode">HPSNode</a>
                <ul>
                    <li><a href="hpsolver.hps.md#add_nodes">add_nodes()</a></li>
                    <li><a href="hpsolver.hps.md#del_nodes">del_nodes()</a></li>
                    <li><a href="hpsolver.hps.md#get_nodes">get_nodes()</a></li>
                    <li><a href="hpsolver.hps.md#set_nodes">set_nodes()</a></li>
                    <li><a href="hpsolver.hps.md#run_nodes">run_nodes()</a></li>
                    <li><a href="hpsolver.hps.md#get_tree">get_tree()</a></li>
                    <li><a href="hpsolver.hps.md#make_sol">make_sol()</a></li>
                    <li><a href="hpsolver.hps.md#make_opr">make_opr()</a></li>
                    <li><a href="hpsolver.hps.md#make_dtn_leaf">make_dtn_leaf()</a></li>
                    <li><a href="hpsolver.hps.md#make_sol_leaf">make_sol_leaf()</a></li>
                </ul>
            </li>
            <li><a href="hpsolver.hps.md#hpsdata">HPSData</a>
                <ul>
                    <li><a href="hpsolver.hps.md#new_body_west">new_body_west()</a></li>
                    <li><a href="hpsolver.hps.md#new_body_east">new_body_east()</a></li>
                    <li><a href="hpsolver.hps.md#new_body_join">new_body_join()</a></li>
                    <li><a href="hpsolver.hps.md#mat_from_body">mat_from_body()</a></li>
                    <li><a href="hpsolver.hps.md#vec_from_body">vec_from_body()</a></li>
                    <li><a href="hpsolver.hps.md#make_sol-1">make_sol()</a></li>
                </ul>
            </li>
            <li><a href="hpsolver.hps.md#hpsgeom">HPSGeom</a></li>
            <li><a href="hpsolver.hps.md#hpspoisson">HPSPoisson</a></li>
        </ul>
    </li>
</ul>
</p>

### hpsolver.polys

<p>
<ul class="ref-list" id="mod-refs">
    <li><a href="hpsolver.polys.md#hpsolver.polys">hpsolver.polys</a>
        <ul>
            <li><a href="hpsolver.polys.md#polybasis">PolyBasis</a>
                <ul>
                    <li><a href="hpsolver.polys.md#polys">polys()</a></li>
                    <li><a href="hpsolver.polys.md#derivs">derivs()</a></li>
                    <li><a href="hpsolver.polys.md#integax">integax()</a></li>
                    <li><a href="hpsolver.polys.md#integxb">integxb()</a></li>
                </ul>
            </li>
            <li><a href="hpsolver.polys.md#polyopr">PolyOpr</a>
                <ul>
                    <li><a href="hpsolver.polys.md#with_nodes">with_nodes()</a></li>
                    <li><a href="hpsolver.polys.md#with_polys">with_polys()</a></li>
                    <li><a href="hpsolver.polys.md#asdict">asdict()</a></li>
                    <li><a href="hpsolver.polys.md#asmat">asmat()</a></li>
                </ul>
            </li>
            <li><a href="hpsolver.polys.md#nodeset">NodeSet</a></li>
            <li><a href="hpsolver.polys.md#legendre">Legendre</a></li>
            <li><a href="hpsolver.polys.md#chebyshev">Chebyshev</a></li>
            <li><a href="hpsolver.polys.md#lgngauss">lgngauss()</a></li>
            <li><a href="hpsolver.polys.md#lbtgauss">lbtgauss()</a></li>
            <li><a href="hpsolver.polys.md#chbgauss">chbgauss()</a></li>
            <li><a href="hpsolver.polys.md#chblobatto">chblobatto()</a></li>
        </ul>
    </li>
</ul>
</p>