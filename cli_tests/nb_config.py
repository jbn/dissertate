import dissertate

c = get_config()

c.Exporter.preprocessors = ['dissertate.preprocessors.CellElider',
                            'dissertate.preprocessors.EmptyCellElider']

c.Exporter.template_file = dissertate.markdown_template_path()
