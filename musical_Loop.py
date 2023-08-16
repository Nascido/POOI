
samples = int(input())
samples_peaks = []

while samples != 0:
    points = (input()).split()
    points.append(points[0])
    points.append(points[1])
    peaks = 0
    
    for i in range(1, samples+1):
        diff0 = int(points[i]) - int(points[i-1])
        diff1 = int(points[i+1]) - int(points[i])

        if diff0 > 0:
            if diff1 < 0:
                peaks += 1
        
        elif diff1 > 0:
            peaks += 1
        
    samples_peaks.append(peaks)
    samples = int(input())

for peaks in samples_peaks:
    print(peaks)
    