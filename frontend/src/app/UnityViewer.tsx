import React from 'react';

export default function UnityViewer() {
  return (
    <iframe
      src="/unity/index.html"
      style={{
        width: '100%',
        height: '80vh',
        border: 'none',
      }}
      title="Unity WebGL Viewer"
      allowFullScreen
    />
  );
}
