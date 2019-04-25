import dissertate

c = get_config()

c.Exporter.preprocessors = ['dissertate.preprocessors.EmptyCellElider',
                            'dissertate.preprocessors.CellElider']

c.Exporter.template_file = dissertate.markdown_template_path()
