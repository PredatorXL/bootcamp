x = int(input('Podaj pozycję x: '))
y = int(input('Podaj pozycję y: '))


if x > 100 or y > 100 or x < 0 or y < 0:       # najpierw sprawdzamy, czy pozycje są poza planszą
    print('Jesteś poza planszą')
elif x > 90 and y > 90:
    print('Jesteś w prawym górnym rogu')
elif x > 90 and y < 10:
    print('Jesteś w prawym dolnym rogu')
elif x < 10 and y < 10:
    print('Jesteś w lewym dolnym rogu')
elif x < 10 and y > 90:
    print('Jesteś w lewym górnym rogu')
elif y < 10:
    print('Jesteś na dolnej krawędzi')
elif y > 90:
    print('Jesteś na górnej krawędzi')
elif x < 10:
    print('Jesteś na lewej krawędzi')
elif x > 90:
    print('Jesteś na prawej krawędzi')
else:
    print('Jesteś w centrum')