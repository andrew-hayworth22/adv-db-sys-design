<h1> List of Pets </h1>
<ul>
    % for pet in data:
        <li>{{ pet[1] }}</li>
    % end
</ul>

<h1> Table of Pets </h1>

<table>
    <thead>
    % for name in names[1:] :
        <th>{{name}}</th>
    % end
    </thead>

    <tbody>
    % for pet in data :
        <tr>
            <td>{{pet[1]}}</td>
            <td>{{pet[2]}}</td>
        </tr>
    % end
    </tbody>
</table>