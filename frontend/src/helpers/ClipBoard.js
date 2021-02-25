export const copy = text => {
    const mockEl = document.createElement('textarea');
    mockEl.value = text;
    document.body.appendChild(mockEl);
    mockEl.select();
    document.execCommand('copy');
    document.body.removeChild(mockEl);
};