import mahler.core.resources


scheduler = mahler.core.resources.build('local')
print(scheduler.available())

print(scheduler.submit(list(range(100)), tags=['there', 'should', 'be', 'none']))
