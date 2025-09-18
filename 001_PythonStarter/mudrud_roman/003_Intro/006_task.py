day = input('Input day of week: ').lower()
work_day = 'Today on work'
day_off = 'Today is a day off'
match day:
    case 'monday':
        print(work_day)
    case 'tuesday':
        print(work_day)
    case 'wednesday':
        print(work_day)
    case 'thursday':
        print(work_day)
    case 'friday':
        print(work_day)
    case 'saturday':
        print(day_off)
    case 'sunday':
        print(day_off)
    case _ :
        print('There is no such day')

    