results.map((result) => ({
  status: result.status,
  value: result.value || result.reason.toString(),
}))
