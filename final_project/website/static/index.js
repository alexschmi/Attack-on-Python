function deleteReservation(reservationId) {
  fetch("/delete-reservation", {
    method: "POST",
    body: JSON.stringify({ reservationId: reservationId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}