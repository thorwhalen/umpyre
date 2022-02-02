# Problem: Where should I put my test dependencies

Someone broke the CI again because they used `whatever` package for testing, but it wasn't mentioned in `setup.cfg` requirements. 
But they SHOULD NOT list it there because it's a requirement for testing only. 
So where SHOULD they mention it?

# Solution: Several options

- Include in [options.extras_require] section of setup.cfg (https://stackoverflow.com/questions/58826164/dependencies-requirements-for-setting-up-testing-and-installing-a-python-lib). Not sure exactly what this section does though (@channel, anything to add?)
- Include in the "Install dependencies of the CI definition (e.g. `ci.yml`) of the project. Same place where `pytest`, `pylint`, `isee` are... (Though here I'd ask the quest as to whether it would be better to have a different section for these "EXTRAS" that are project-specific. Would help to keep things separate and organized -- easier for update/maintenance of the ci.yml definition.)

Don't know what the best practice is, or pros/cons around the question.
