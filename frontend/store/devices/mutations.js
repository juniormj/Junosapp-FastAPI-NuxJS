export default {
  SET_BRAS(state, bras) {
    state.bras = bras;
  },
  PUT_DEVICE(state, deviceEdit) {
    state.deviceEdit = deviceEdit;
  },
  SET_DEVICE(state, deviceEdit) {
    state.deviceEdit = deviceEdit;
  },
  SET_DEVICE_UPDATE(state, deviceEdit) {
    state.deviceEdit = Object.assign({}, state.deviceEdit, deviceEdit);
  },
};
