{% extends 'markdown.tpl'%}

{% block data_svg %}
![{{cell.metadata.caption if cell.metadata.caption else 'svg'}}]({{ output.metadata.filenames['image/svg+xml'] | path2url }})
{% endblock data_svg %}

{% block data_png %}
![{{cell.metadata.caption if cell.metadata.caption else 'png'}}]({{ output.metadata.filenames['image/png'] | path2url }})
{% endblock data_png %}

{% block data_jpg %}
![{{cell.metadata.caption if cell.metadata.caption else 'jpg'}}]({{ output.metadata.filenames['image/jpeg'] | path2url }})
{% endblock data_jpg %}