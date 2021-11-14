from Plot_time_web_cam import plot_graph
from bokeh.plotting import output_file, show
import cv2
from datetime import datetime
import pandas

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, first_frame = video.read()
# cv2.imshow("First Frame", first_frame)
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21, 21), 0)
first_frame_time = datetime.now()
movement_detected_time = None

movement_statuses = [False, False]
movement_change_time_list = []
time_df = pandas.DataFrame(columns=["Start", "End"])

while True:
    movement_status = False
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("Color Frame", frame)
    # cv2.imshow("Gray Frame", gray)
    blurred_frame = cv2.GaussianBlur(gray, (21, 21), 0)
    # cv2.imshow("Blurred Frame", blurred_frame)
    delta = cv2.absdiff(first_frame, blurred_frame)
    # cv2.imshow("Delta Frame", delta)
    threshold_frame = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Threshold Frame", threshold_frame[1])

    contours, _ = cv2.findContours(threshold_frame[1].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        movement_detected_time = datetime.now()
        movement_status = True
        # print(movement_detected_time)

    movement_statuses.append(movement_status)
    if movement_statuses[-2] != movement_statuses[-1]:
        print("Status Changed")
        movement_change_time_list.append(datetime.now())
    cv2.imshow("Color Outline Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(movement_statuses)
print(movement_change_time_list)
print({"Start": movement_change_time_list[0]})

for i in range(0, len(movement_change_time_list), 2):
    time_df = time_df.append({"Start": movement_change_time_list[i], "End": movement_change_time_list[i + 1]},
                             ignore_index=True)

# print(time_df)
plot_graph(time_df)
time_df.to_csv("Times_list.csv")
video.release()
cv2.destroyAllWindows()

# #
#    Record the time when the object appears into the frame
# #

